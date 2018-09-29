# encoding: utf-8

from rest_framework import serializers
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.medal.models import *
from follow.models import *


class Userfollow2Serializers(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ("username",)


class UserfollowSerializers(serializers.ModelSerializer):
	user_follow = Userfollow2Serializers()

	class Meta:
		model = Userfollow
		fields = ("user_follow",)


class ToUserProfileSerializers(serializers.ModelSerializer):
	user = Userfollow2Serializers()

	class Meta:
		model = Userfollow
		fields = ("user",)


class MedalSerializers(serializers.ModelSerializer):
	class Meta:
		model = Medal
		fields = ("name", "pathwel")


class UserMedalSerializers(serializers.ModelSerializer):
	medal = MedalSerializers()

	class Meta:
		model = UserMedal
		fields = ("medal",)


class UserProfileSerializers(serializers.ModelSerializer):
	UserMedals = UserMedalSerializers(many=True, read_only=True)
	UserProfile = UserfollowSerializers(many=True, read_only=True)
	ToUserProfile = ToUserProfileSerializers(many=True, read_only=True)

	class Meta:
		model = UserProfile
		fields = ("username", "icon", "signature", "UserMedals", "UserProfile", "ToUserProfile")


class UserCenterViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		查看用户个人信息+勋章+关注
	"""
	authentication_classes = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	serializer_class = UserProfileSerializers

	def get_queryset(self):
		return UserProfile.objects.filter(username=self.request.user)
