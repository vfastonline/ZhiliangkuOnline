# encoding: utf-8
from rest_framework import authentication
from rest_framework import mixins
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import *

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("name", "email")


class UserPagination(PageNumberPagination):
	page_size = 100


class ConsultantViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取咨询师信息
	"""
	queryset = User.objects.filter(role__index=4)
	serializer_class = UserSerializer
	pagination_class = UserPagination
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)
