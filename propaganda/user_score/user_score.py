# encoding: utf-8

from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_score.exception import NoneTeamUnavailable
from user_score.user_score_create_serializers import AddUserScoreSerializers
from user_score.user_score_retrieve_serializers import GetUserScoreRecordSerializers

User = get_user_model()


class UserScoreViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
	"""
	create:
		添加登录用户的评分记录
	read:
		获取登录用户的评分记录
	"""
	authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		if self.action == "create":
			return AddUserScoreSerializers
		return GetUserScoreRecordSerializers

	def get_queryset(self):
		if not self.request.user.team.exists():
			raise NoneTeamUnavailable
		return User.objects.filter(username=self.request.user)
