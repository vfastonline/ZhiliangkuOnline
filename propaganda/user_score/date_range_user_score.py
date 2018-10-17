# encoding: utf-8

from django_filters import rest_framework as filters
from rest_framework import authentication, serializers
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import *


class UserScoreDateFilter(filters.FilterSet):
	"""
	用户评分记录时间过滤
	"""
	start_date = filters.DateFromToRangeFilter(field_name="created_at", label="开始时间")
	end_date = filters.DateFromToRangeFilter(field_name="created_at", label="结束时间")
	team = filters.CharFilter(field_name="owner__team", label="班级_id")

	class Meta:
		model = UserScore
		fields = ['start_date', 'end_date', 'team']


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
