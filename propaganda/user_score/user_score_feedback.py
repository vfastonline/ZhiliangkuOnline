# encoding: utf-8
from rest_framework import authentication, serializers
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_score.permissions import BrowseScoreReportPermission
from .filter import *


class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["username", "icon"]


class UserScoreSerializers(serializers.ModelSerializer):
	owner = UserSerializers()
	created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

	class Meta:
		model = UserScore
		fields = ["feedback", "owner", "created_at"]


class UserScoreFeedbackViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取用户评分反馈，支持时间过滤
	"""
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated, BrowseScoreReportPermission)
	queryset = UserScore.objects.all()
	serializer_class = UserScoreSerializers
	filter_class = UserScoreDateFilter
