# encoding: utf-8
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import serializers
from rest_framework import viewsets

from directory_tree.models import *
from technical_label.models import *
from .models import Project


class TechnicalLabelSerializer(serializers.ModelSerializer):
	class Meta:
		model = TechnicalLabel
		fields = ["name", ]


class DirectoryTreeSerializer(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = DirectoryTree
		fields = ["_id", ]


class ProjectSerializer(serializers.ModelSerializer):
	"""
	项目
	"""
	_id = serializers.CharField(max_length=24)
	project = serializers.SerializerMethodField(read_only=True)
	technical_labels = serializers.SerializerMethodField(read_only=True)

	direction = serializers.HiddenField(
		default=DirectoryTreeSerializer(read_only=True)
	)

	def get_technical_labels(self, obj):
		name = obj.technical_labels
		name_json = TechnicalLabelSerializer(name, many=True, context={'request': self.context['request']}).data
		return name_json

	def get_project(self, obj):
		name = obj.project.name
		return name

	class Meta:
		model = Project
		fields = ["_id", "project", "direction", "technical_labels", "image", "desc", "price", "study", "course",
				  "section", "stars", "hot",
				  "new"]


class ProjectViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取方向下项目
	"""
	queryset = Project.objects.filter()
	serializer_class = ProjectSerializer
	authentication_classes = ()
	permission_classes = ()
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ("direction",)
