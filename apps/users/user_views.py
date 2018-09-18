# encoding: utf-8

from rest_framework import mixins, viewsets
from rest_framework import permissions, authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from user_resumes.models import UserResume
from utils.drf_response_handler import *
from .serializers import *


class UserViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	"""
	用户
	"""
	serializer_class = UserRegSerializer
	queryset = User.objects.all()
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

	def get_serializer_class(self):
		if self.action == "retrieve":
			return UserDetailSerializer
		elif self.action == "create":
			return UserRegSerializer
		elif self.action == "update" or self.action == "partial_update":
			return UserUpdateSerializer

		return UserRegSerializer

	def get_permissions(self):
		if self.action == "retrieve":
			return [permissions.IsAuthenticated()]
		elif self.action == "create":
			return []

		return []

	def perform_create(self, serializer):
		user = serializer.save()

		# 页面注册成功后，增加默认简历
		UserResume.objects.create(user=user)
		return user

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = self.perform_create(serializer)

		re_dict = serializer.data
		payload = jwt_payload_handler(user)
		re_dict["token"] = jwt_encode_handler(payload)
		re_dict["name"] = user.name if user.name else user.username

		headers = self.get_success_headers(serializer.data)
		return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

	# 重写该方法，不管传什么id，都只返回当前用户
	def get_object(self):
		return self.request.user
