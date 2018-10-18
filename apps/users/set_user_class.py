# encoding: utf-8
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Team

User = get_user_model()


class SetUserClassSerializers(serializers.ModelSerializer):
	team_id = serializers.PrimaryKeyRelatedField(label="班级", queryset=Team.objects.all(), write_only=Team,
												 required=True)

	class Meta:
		model = User
		fields = ["name", "team_id"]


class SetUserClassViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
	"""
	update:
		设置用户班级信息
	"""

	authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = SetUserClassSerializers
