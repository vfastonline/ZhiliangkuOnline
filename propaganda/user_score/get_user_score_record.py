# encoding: utf-8
import datetime

from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_score.exception import NoneTeamUnavailable
from .models import ScoreItem
from .models import UserScore

User = get_user_model()


class ScoreItemSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)
	score = serializers.SerializerMethodField()

	def get_score(self, obj):
		return 0

	class Meta:
		model = ScoreItem
		fields = ["_id", "name", "score"]


class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["username", "name", "icon"]


class ScoreRecordSerializers(serializers.Serializer):
	name = serializers.SerializerMethodField()
	score = serializers.IntegerField()

	def get_name(self, obj):
		return obj.score_item.name


class GetUserScoreRecordSerializers(serializers.Serializer):
	is_history = serializers.SerializerMethodField()
	teacher = serializers.SerializerMethodField()
	student = serializers.SerializerMethodField()
	feedback = serializers.SerializerMethodField()

	@staticmethod
	def get_today_user_scores(obj):
		print(222)
		today = datetime.datetime.today()
		start_time = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
		end_time = datetime.datetime(today.year, today.month, today.day, 23, 59, 59)
		filter_param = {
			"owner": obj,
			"created_at__range": [start_time, end_time]
		}
		return UserScore.objects.filter(**filter_param)

	def get_is_history(self, obj):
		"""是否是评分历史记录
		:param obj:
		:return:
		"""
		user_scores = self.get_today_user_scores(obj)
		return user_scores.exists()

	def get_teacher(self, obj):
		return_json = dict()
		teacher_scores = self.get_today_user_scores(obj).exclude(user=obj)
		if teacher_scores.exists():
			user_scores_list = ScoreRecordSerializers(teacher_scores.first().score_records, many=True,
													  context={'request': self.context['request']}).data
		else:
			score_items = ScoreItem.objects.filter(role='2')
			user_scores_list = ScoreItemSerializers(score_items, many=True).data

		teacher_user = obj.team.first().team_users.filter(role__index=1)
		teacher_info = UserSerializers(teacher_user.first(), context={'request': self.context['request']}).data

		return_json["user_info"] = teacher_info
		return_json["score_records"] = user_scores_list
		return return_json

	def get_student(self, obj):
		return_json = dict()
		student_scores = self.get_today_user_scores(obj).filter(user=obj)
		if student_scores.exists():
			user_scores_list = ScoreRecordSerializers(student_scores.first().score_records, many=True,
													  context={'request': self.context['request']}).data
		else:
			score_items = ScoreItem.objects.filter(role='1')
			user_scores_list = ScoreItemSerializers(score_items, many=True).data
		teacher_info = UserSerializers(obj, context={'request': self.context['request']}).data

		return_json["user_info"] = teacher_info
		return_json["score_records"] = user_scores_list
		return return_json

	def get_feedback(self, obj):
		user_scores = self.get_today_user_scores(obj)
		if user_scores.exclude(user=obj).exists():
			return user_scores.first().feedback
		return ""


class GetUserScoreRecordViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取评分项、班主任评分记录
	"""

	authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	serializer_class = GetUserScoreRecordSerializers

	def get_queryset(self):
		if not self.request.user.team.exists():
			raise NoneTeamUnavailable
		return User.objects.all()
