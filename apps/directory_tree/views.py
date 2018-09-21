# encoding: utf-8
from rest_framework import mixins
from rest_framework import viewsets

from .models import DirectoryTree
from .serializers import DirectoryTreeDirectionSerializer


class DirectoryTreeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取指定类型下banner信息列表

	read:
		获取指定类型下某个banner信息
	"""
	queryset = DirectoryTree.objects.filter(category_type="direction")
	serializer_class = DirectoryTreeDirectionSerializer
	authentication_classes = ()
	permission_classes = ()
