# encoding: utf-8

import datetime

from rest_framework import authentication, serializers
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import *

User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["username", "name", "icon"]


class ScoreItemSerializers(serializers.ModelSerializer):
	class Meta:
		model = ScoreItem
		fields = ["name", "role"]


class ScoreRecordSerializers(serializers.Serializer):
	score_item = serializers.SerializerMethodField()
	score = serializers.IntegerField()

	def get_score_item(self, obj):
		return obj.score_item.name


class UserScoreSerializers(serializers.Serializer):
	feedback = serializers.CharField()
	user = UserSerializers()
	role = serializers.SerializerMethodField()
	score_records = ScoreRecordSerializers(many=True)

	def get_role(self, obj):
		if obj.user == obj.owner:
			return "学生"
		return "老师"


class TodayHasUserScoreRecordViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		查看用户今日评分结果
	"""
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	serializer_class = UserScoreSerializers

	def get_queryset(self):
		today = datetime.datetime.today()
		start_time = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
		end_time = datetime.datetime(today.year, today.month, today.day, 23, 59, 59)
		filter_param = {
			"owner": self.request.user,
			"created_at__range": [start_time, end_time]
		}
		return UserScore.objects.filter(**filter_param)
