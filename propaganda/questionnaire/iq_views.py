# encoding: utf-8
from rest_framework import mixins
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import *

from .models import *
from .serializers import QuestionnaireScoreSerializer


class IQSerializer(serializers.ModelSerializer):
	option = serializers.ListField()

	class Meta:
		model = IQ
		fields = ("title", "image", "option")


class IQPagination(PageNumberPagination):
	page_size = 100


class IQViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取指IQ测试题

	"""
	queryset = IQ.objects.all()
	serializer_class = IQSerializer
	# authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	# permission_classes = (IsAuthenticated,)
	authentication_classes = ()
	permission_classes = ()
	pagination_class = IQPagination
	throttle_classes = (UserRateThrottle, AnonRateThrottle)

	def get_serializer_class(self):
		if self.action == "list":
			return IQSerializer
		if self.action == "create":
			return QuestionnaireScoreSerializer
		return IQSerializer
