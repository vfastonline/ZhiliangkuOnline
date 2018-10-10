# encoding: utf-8

from rest_framework import authentication
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_operation.user_info_serializers import *


class UserInfoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		查看用户个人信息+勋章+关注
	"""
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	serializer_class = UserProfileSerializers

	def get_queryset(self):
		return UserProfile.objects.filter(username=self.request.user)
