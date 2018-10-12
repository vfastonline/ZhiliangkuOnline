#!encoding:utf-8

from bson.objectid import ObjectId
from rest_framework import serializers, authentication
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_operation.models import *

User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("username", "name")


class FollowUserSerializers(serializers.ModelSerializer):
	user = serializers.CharField(
		default=serializers.CurrentUserDefault()
	)
	follows = serializers.SerializerMethodField()

	def get_follows(self, follow_user):
		users = User.objects.filter(pk__in=[user.user._id for user in follow_user.follows])
		users_json = UserSerializers(users, many=True, context={'request': self.context['request']}).data
		return users_json

	class Meta:
		model = FollowUser
		fields = ("user", "follows")


class FollowUserCreateSerializers(serializers.ModelSerializer):
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)

	follows = serializers.CharField(label="被关注用户", max_length=24, min_length=24, required=True, help_text="被关注用户_id")

	def create(self, validated_data):
		user = validated_data["user"]

		follow_users = FollowUser.objects.filter(user=user)
		if not follow_users.exists():
			validated_data["follows"] = [validated_data["follows"]]
			follow_user = super(FollowUserCreateSerializers, self).create(validated_data=validated_data)
		else:
			follow_user = follow_users[0]
			if follow_users.filter(follows={"user_id": ObjectId(self.initial_data["follows"])}).exists():
				return follow_user
			follow_user.follows.append(validated_data["follows"])
			follow_user.save()
		return follow_user

	def validate_follows(self, follows):
		users = User.objects.filter(pk=follows)
		if not users.exists():
			raise serializers.ValidationError("被关注用户不存在")

		follow_obj = Follow(user=users[0])
		return follow_obj

	class Meta:
		model = FollowUser
		fields = ("user", "follows")


class FollowUserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
						viewsets.GenericViewSet):
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = FollowUser.objects.all()
	serializer_class = FollowUserSerializers

	def get_serializer_class(self):
		if self.action == "create":
			return FollowUserCreateSerializers
		else:
			return FollowUserSerializers
