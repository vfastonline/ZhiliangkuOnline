# encoding: utf-8

from datetime import datetime, timedelta

from rest_framework import authentication, serializers
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_score.permissions import BrowseScoreReportPermission
from users.models import Team
from .filter import *


class ScoreItemAvgSerializers(serializers.Serializer):
	name = serializers.SerializerMethodField()
	avg = serializers.FloatField()

	def get_name(self, obj):
		score_item_dict = self.context["score_item_dict"]  # {"_id": "name"}
		return score_item_dict.get(str(obj.get("name")))


class UserScoreItemAvgSerializers(serializers.Serializer):
	_id = serializers.CharField()
	avg_list = ScoreItemAvgSerializers(many=True)


class ScoreItemSerializers(serializers.ModelSerializer):
	_id = serializers.CharField()

	class Meta:
		model = ScoreItem
		fields = ["_id", "name"]


class UserScoreItemAvgViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		查询班级评分项平均值
	"""
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated, BrowseScoreReportPermission)
	serializer_class = UserScoreItemAvgSerializers
	filter_class = UserScoreDateFilter
	queryset = UserScore.objects.all()

	def get_serializer(self, *args, **kwargs):
		score_item_list = ScoreItemSerializers(ScoreItem.objects.all(), many=True).data
		score_item_dict = {one["_id"]: one["name"] for one in score_item_list}
		serializer_class = self.get_serializer_class()
		kwargs['context'] = self.get_serializer_context()
		kwargs['context'].update({"score_item_dict": score_item_dict})
		return serializer_class(*args, **kwargs)

	def list(self, request, *args, **kwargs):
		today = datetime.today()
		six_day_ago = datetime.today() - timedelta(days=6)
		query_params = request.query_params
		created_at_after = query_params.get("created_at_after")
		if created_at_after:
			created_at_after = datetime.strptime(created_at_after, "%Y-%m-%d")
		else:
			created_at_after = six_day_ago
		created_at_before = query_params.get("created_at_before")
		if created_at_before:
			created_at_before = datetime.strptime(created_at_before, "%Y-%m-%d")
		else:
			created_at_before = today
		team = query_params.get("team")

		start_time = datetime(created_at_after.year, created_at_after.month, created_at_after.day, 0, 0, 0)
		end_time = datetime(created_at_before.year, created_at_before.month, created_at_before.day, 23, 59, 59)
		team_user_id_list = Team.objects.filter(pk=team).first().team_users.all().values_list("_id", flat=True)

		queryset = UserScore.objects.mongo_aggregate([
			{"$match": {
				"created_at": {'$gte': start_time, '$lte': end_time},
				"user_id": {"$in": list(team_user_id_list)}
			}},
			{"$unwind": "$score_records"},
			{"$group": {
				"_id": {
					"item_id": "$score_records.score_item_id",
					"created_at": {"$dateToString": {"format": "%Y-%m-%d", "date": "$created_at"}}},
				"AvgScore": {"$avg": "$score_records.score"}}},
			{"$project": {
				"created_at": "$_id.created_at",
				"sub_info": {"name": "$_id.item_id", "avg": "$AvgScore"}}},
			{"$group": {"_id": "$created_at", "avg_list": {"$push": "$sub_info"}}}
		])
		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)
