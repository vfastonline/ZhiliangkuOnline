# encoding: utf-8
# from rest_framework import authentication
from rest_framework import mixins
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import *
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import QuestionnaireScoreSerializer
from .models import *


class EQSerializer(serializers.ModelSerializer):
	option = serializers.ListField()

	class Meta:
		model = EQ
		fields = ("title", "option")


class EQPagination(PageNumberPagination):
	page_size = 100


class EQViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取指EQ测试题

	"""
	queryset = EQ.objects.all()
	serializer_class = EQSerializer
	# authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	# permission_classes = (IsAuthenticated,)
	authentication_classes = ()
	permission_classes = ()
	pagination_class = EQPagination
	throttle_classes = (UserRateThrottle, AnonRateThrottle)

	def get_serializer_class(self):
		if self.action == "create":
			return QuestionnaireScoreSerializer
		if self.action == "list":
			return EQSerializer
		return EQSerializer
