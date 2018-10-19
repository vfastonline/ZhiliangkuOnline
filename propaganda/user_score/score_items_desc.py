# encoding: utf-8
from rest_framework import mixins, viewsets, serializers, authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import *


class ScoreItemSerializers(serializers.ModelSerializer):
	class Meta:
		model = ScoreItem
		fields = ["name", "desc", ]


class ScoreItemsDescViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取得分项详细说明
	"""
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = ScoreItem.objects.all()
	serializer_class = ScoreItemSerializers
