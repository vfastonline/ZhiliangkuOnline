from rest_framework import serializers

from .models import *


class DirectoryTreeVideoSerializer(serializers.ModelSerializer):
	"""
	视频
	"""
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = DirectoryTree
		fields = ["_id", "category", "name"]


class DirectoryTreeSectionSerializer(serializers.ModelSerializer):
	"""
	章节
	"""
	_id = serializers.CharField(max_length=24)
	sub_category = DirectoryTreeVideoSerializer(many=True)

	class Meta:
		model = DirectoryTree
		fields = ["_id", "category", "name", "sub_category"]


class DirectoryTreeCourseSerializer(serializers.ModelSerializer):
	"""
	课程
	"""
	_id = serializers.CharField(max_length=24, read_only=True)
	sub_category = DirectoryTreeSectionSerializer(many=True)

	class Meta:
		model = DirectoryTree
		fields = ["_id", "category", "name", "sub_category"]


class DirectoryTreeProjectSerializer(serializers.ModelSerializer):
	"""
	项目
	"""
	_id = serializers.CharField(max_length=24, read_only=True)
	sub_category = DirectoryTreeCourseSerializer(many=True, read_only=True)

	class Meta:
		model = DirectoryTree
		fields = ["_id", "category", "name", "sub_category"]


class DirectoryTreeDirectionSerializer(serializers.ModelSerializer):
	"""
	项目
	"""
	_id = serializers.CharField(max_length=24, read_only=True)
	sub_category = DirectoryTreeProjectSerializer(many=True, read_only=True)

	class Meta:
		model = DirectoryTree
		fields = ["_id", "category", "name", "sub_category"]
