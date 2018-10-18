# encoding: utf-8

from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_operation.user_info_serializers import *

User = get_user_model()


class UserPersonalInfoSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("name",)


class UserPersonalInfoViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	"""
	read:
		用户个人信息
	"""
	authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	serializer_class = UserPersonalInfoSerializers

	def get_queryset(self):
		return User.objects.filter(username=self.request.user)
