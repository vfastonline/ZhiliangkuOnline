# encoding: utf-8

from rest_framework import authentication, serializers
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import *


class ScoreRecordSerializers(serializers.Serializer):
	score_item = serializers.PrimaryKeyRelatedField(label="评分项", queryset=ScoreItem.objects.all())
	score = serializers.IntegerField()


class AddUserScoreSerializers(serializers.Serializer):
	owner = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)
	user = serializers.PrimaryKeyRelatedField(label="用户", required=True, queryset=User.objects.all(), help_text="老师或学生")
	score_records = ScoreRecordSerializers(many=True, required=True)
	feedback = serializers.CharField(label="反馈", help_text="用户反馈")

	def create(self, validated_data):
		score_records = validated_data["score_records"]
		validated_data["score_records"] = [ScoreRecord(score_item=one_score["score_item"], score=one_score["score"]) for
										   one_score in score_records]
		user_score_obj = UserScore.objects.create(**validated_data)
		return user_score_obj


class AddUserScoreViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
	"""
	create:
		添加用户评分记录
	"""
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = UserScore.objects.all()
	serializer_class = AddUserScoreSerializers
