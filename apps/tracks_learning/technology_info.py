#!encoding:utf-8

from rest_framework import serializers
from rest_framework import viewsets, mixins

from tracks_learning.models import *


class TechnologySerializer(serializers.ModelSerializer):
	video_id = serializers.CharField()

	class Meta:
		model = Technology
		fields = ("name", "desc", "video_id")


class TechnologyListInfo(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
	查询技术方向
	"""
	authentication_classes = ()
	permission_classes = ()

	queryset = Technology.objects.all()
	serializer_class = TechnologySerializer
