# encoding: utf-8

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import UserResume

User = get_user_model()


class UserResumeRegSerializer(serializers.ModelSerializer):
	"""
	用户简历'序列化
	"""
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = UserResume
		fields = "__all__"
