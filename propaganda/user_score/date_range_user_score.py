# encoding: utf-8


from rest_framework import authentication, serializers
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .filter import *


class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["username", "icon"]


class UserScoreSerializers(serializers.ModelSerializer):
	owner = UserSerializers()
	feedback = serializers.CharField()
	created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")

	class Meta:
		model = UserScore
		fields = ["feedback", "owner", "created_at"]


class DateRangeUserScoreViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		查看用户评分结果(支持日期、班级条件过滤)
	"""
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = UserScore.objects.all()
	serializer_class = UserScoreSerializers
	filter_class = UserScoreDateFilter
