# encoding: utf-8
from rest_framework import mixins
from rest_framework import serializers
from rest_framework import viewsets

from .models import DirectoryTree


class DirectionSerializer(serializers.ModelSerializer):
	"""
	方向
	"""
	_id = serializers.CharField(max_length=24, read_only=True)

	class Meta:
		model = DirectoryTree
		fields = ["_id", "name"]


class DirectionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取方向
	"""
	queryset = DirectoryTree.objects.filter(category="direction")
	serializer_class = DirectionSerializer
	authentication_classes = ()
	permission_classes = ()
