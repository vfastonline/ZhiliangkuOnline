# encoding: utf-8

from rest_framework import mixins, viewsets
from rest_framework import permissions, authentication
from rest_framework.mixins import CreateModelMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from users.serializers import *


class UserViewSet(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	"""
	用户
	"""
	serializer_class = UserRegSerializer
	queryset = User.objects.all()
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

	def get_serializer_class(self):
		if self.action == "retrive":
			return UserDetailSerializer
		elif self.action == "create":
			return UserRegSerializer

		return UserRegSerializer

	# permission_classes = (permissions.IsAuthenticated, )
	def get_permissions(self):
		if self.action == "retrieve":
			return [permissions.IsAuthenticated()]
		elif self.action == "create":
			return []

		return []
