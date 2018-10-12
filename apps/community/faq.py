#!encoding:utf-8

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import authentication
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from community.faq_serializers import *


class FaqViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取用户问题
	create:
		添加用户问题
	delete:
		删除用户问题

	"""
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = Faq.objects.all()

	filter_backends = (DjangoFilterBackend,)
	filter_fields = ("user_id",)

	def get_serializer_class(self):
		if self.action == "create":
			return FaqCreateSerializers
		else:
			return FaqSerializers


class SpecifyFaqViewSet(mixins.RetrieveModelMixin,viewsets.GenericViewSet):
	"""
	read:
		获取指定问题
	"""
	authentication_classes = ()
	permission_classes = ()
	serializer_class = FaqSerializers
	queryset = Faq.objects.all()


