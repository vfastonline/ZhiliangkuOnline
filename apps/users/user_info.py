# encoding: utf-8

from django.contrib.auth import get_user_model
from rest_framework import serializers, authentication
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Team, Role

User = get_user_model()


class TeamSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = Team
		fields = ("_id", "name")


class RoleSerializers(serializers.ModelSerializer):
	class Meta:
		model = Role
		fields = ("name",)


class UserSerializers(serializers.ModelSerializer):
	team = TeamSerializers(many=True, read_only=True)

	class Meta:
		model = User
		fields = (
			"name", "gender", "birthday", "icon", "institution", "computer_major", "graduate", "education",
			"signature", "mobile", 'team')


class UserUpdateSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
			"name", "gender", "birthday", "icon", "institution", "computer_major", "graduate", "education",
			"signature", "mobile")


class UserListSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)
	team = TeamSerializers(many=True, read_only=True)
	role = RoleSerializers(many=True, read_only=True)

	class Meta:
		model = User
		fields = (
			"_id", "username", "gender", "birthday", "team", "role", "institution", "computer_major", "graduate",
			"education",
			"signature", "mobile")


class UserInfoViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
					  viewsets.GenericViewSet):
	"""
	list:
		获取用户信息
	read:
		获取指定用户信息
	update:
		更改用户信息
	partial_update:
		更改用户信息(允许只更新部分字段)

	"""
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return User.objects.filter(username=self.request.user)

	def get_serializer_class(self):
		if self.action == 'list':
			return UserListSerializers
		if self.action == "retrieve":
			return UserSerializers
		return UserUpdateSerializers
