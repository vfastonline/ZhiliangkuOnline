# encoding: utf-8
from rest_framework import mixins
from rest_framework import serializers
from rest_framework import viewsets

from directory_tree.models import DirectoryTree


class DirectoryTreeProjectSerializer(serializers.ModelSerializer):
	"""
	项目
	"""
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = DirectoryTree
		fields = ["_id", "category", "name"]


class DirectoryTreeDirectionSerializer(serializers.ModelSerializer):
	"""
	方向
	"""
	_id = serializers.CharField(max_length=24)
	sub_category = DirectoryTreeProjectSerializer(many=True, read_only=True)

	class Meta:
		model = DirectoryTree
		fields = ["_id", "name", "sub_category"]


class ProjectViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	"""
	read:
		获取方向下项目
	"""
	queryset = DirectoryTree.objects.filter()
	serializer_class = DirectoryTreeDirectionSerializer
	authentication_classes = ()
	permission_classes = ()
