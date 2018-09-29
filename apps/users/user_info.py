# encoding: utf-8

from rest_framework import serializers
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import UserProfile, Team, Role


class TeamSerializers(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = ("name",)


class RoleSerializers(serializers.ModelSerializer):
	class Meta:
		model = Role
		fields = ("name",)


class UserProfileCreateSerializers(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = (
			"name", "gender", "birthday", "icon", "institution", "computer_major", "graduate", "education",
			"signature", "mobile")


class UserProfileSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)
	team = TeamSerializers(many=True, read_only=True)
	role = RoleSerializers(many=True, read_only=True)

	class Meta:
		model = UserProfile
		fields = (
			"_id", "username", "gender", "birthday", "team", "role", "institution", "computer_major", "graduate",
			"education",
			"signature", "mobile")

# def get_team(self,obj):
# 	obj.team.filter(code=)


class UserInfoViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
					  viewsets.GenericViewSet):
	"""
	list:
		获取用户信息
	update:
		更改用户信息
	partial_update:
		更改用户信息(允许只更新部分字段)
	delete:
		删除用户信息

	"""
	authentication_classes = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return UserProfile.objects.filter(username=self.request.user)

	def get_serializer_class(self):
		if self.action == 'list':
			return UserProfileSerializers
		elif self.action != "list":
			return UserProfileCreateSerializers
