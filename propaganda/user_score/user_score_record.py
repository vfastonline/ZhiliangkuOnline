# encoding: utf-8
import datetime

from rest_framework import authentication, serializers
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import *


class UserScoreSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = UserScore
		fields = ["_id", ]


class UserScoreRecordViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		查看用户时间段内评分记录
	"""
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	serializer_class = UserScoreSerializers

	def get_queryset(self):
		today = datetime.datetime.today()
		start_time = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
		end_time = datetime.datetime(today.year, today.month, today.day, 23, 59, 59)
		filter_param = {
			"user": self.request.user,
			"created_at__range": [start_time, end_time]
		}
		return UserScore.objects.filter(**filter_param)
