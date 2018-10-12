#!encoding:utf-8
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import authentication
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from community.faq_answer_serializers import *


class FaqAnswerViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
					   viewsets.GenericViewSet):
	"""
	list:
		获取问题答案
	create:
		添加问题答案
	delete:
		删除问题答案
	"""
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = FaqAnswer.objects.all()
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ("user_id", "faq_id")

	def get_serializer_class(self):
		if self.action == 'create':
			return FaqAnswerCreateSerializers
		else:
			return FaqAnswerSerializers


class SpecifyFaqAnswerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取指定问题答案
	"""
	authentication_classes = ()
	permission_classes = ()
	queryset = FaqAnswer.objects.all()
	serializer_class = FaqAnswerSerializers

	filter_backends = (DjangoFilterBackend,)
	filter_fields=("faq_id",)