# encoding: utf-8
from rest_framework import serializers

from medal.models import *
from user_operation.models import *
from users.models import UserProfile


class FollowUserSerializers(serializers.ModelSerializer):
	class Meta:
		model = FollowUser
		fields = ("follows",)


class MedalSerializers(serializers.ModelSerializer):
	class Meta:
		model = Medal
		fields = ("name",)


class UserMedalSerializers(serializers.ModelSerializer):
	medal = MedalSerializers()

	class Meta:
		model = UserMedal
		fields = ("medal",)


class UserProfileSerializers(serializers.ModelSerializer):
	UserMedals = UserMedalSerializers(many=True, read_only=True)
	follow_user_users = FollowUserSerializers(many=True, read_only=True)
	to_follow_user = serializers.SerializerMethodField()

	class Meta:
		model = UserProfile
		fields = ("username", "icon", "signature", "UserMedals", "follow_user_users", "to_follow_user")

	def get_to_follow_user(self, obj):
		to_follow = []
		for follow in FollowUser.objects.values("user__username", "follows"):
			if str(follow["follows"][0]) == obj.username:
				to_follow.append(follow["user__username"])
		return to_follow
