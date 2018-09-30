# encoding: utf-8
from rest_framework import authentication
from rest_framework import mixins
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import *
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import *
from .serializers import QuestionnaireScoreSerializer, OptionSerializer


class EQSerializer(serializers.ModelSerializer):
	option = OptionSerializer(many=True)

	class Meta:
		model = EQ
		fields = ("title", "option")


class EQPagination(PageNumberPagination):
	page_size = 100


class EQViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取指EQ测试题

	create:
		录入成绩
	"""
	queryset = EQ.objects.all()
	serializer_class = EQSerializer
	pagination_class = EQPagination
	# throttle_classes = (UserRateThrottle, AnonRateThrottle)

	def get_authenticators(self):
		if self.request.method == "POST":
			return [JSONWebTokenAuthentication(), authentication.SessionAuthentication()]
		return []

	def get_permissions(self):
		if self.action == "create":
			return [IsAuthenticated()]
		return []

	def get_serializer_class(self):
		if self.action == "create":
			return QuestionnaireScoreSerializer
		if self.action == "list":
			return EQSerializer
		return EQSerializer
