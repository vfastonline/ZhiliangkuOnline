#!encoding:utf-8

from rest_framework import serializers, authentication
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_operation.models import *
from utils.permissions import IsOwnerOrReadOnly

User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = User
		fields = ("_id", "username", "name")


class FollowUserSerializers(serializers.Serializer):
	_id = serializers.CharField(max_length=24, read_only=True)
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)
	follows_user = serializers.PrimaryKeyRelatedField(label="关注用户_id", required=True,
													  queryset=User.objects.all(),
													  write_only=True, help_text="关注用户_id")
	follows = serializers.SerializerMethodField(read_only=True)

	def get_follows(self, follow_user_obj):
		users = [follow.user for follow in follow_user_obj.follows]
		users_json = UserSerializers(users, many=True, context={'request': self.context['request']}).data
		return users_json

	def create(self, validated_data):
		user = validated_data["user"]
		follows_user = validated_data["follows_user"]

		follow_users = FollowUser.objects.filter(user=user)
		if not follow_users.exists():
			create_param = {
				"user": user,
				"follows": [Follow(user=follows_user)]
			}
			follow_user_obj = FollowUser.objects.create(**create_param)
		else:
			follow_user_obj = follow_users[0]
			if follow_users.filter(follows={"user_id": follows_user.pk}).exists():
				return follow_user_obj
			follow_user_obj.follows.append(Follow(user=follows_user))
			follow_user_obj.save()
		return follow_user_obj

	def update(self, instance, validated_data):
		follow_user_id = validated_data["follows_user"].pk
		update_result = FollowUser.objects.mongo_update(
			{"_id": instance.pk},
			{"$pull": {"follows": {"user_id": follow_user_id}}}
		)
		# update_result = {'n': 1, 'nModified': 0, 'ok': 1.0, 'updatedExisting': True}
		instance = FollowUser.objects.get(pk=instance.pk)
		return instance


class FollowUserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
						viewsets.GenericViewSet):
	"""
	list:
		获取用户关注的用户信息

	create:
		关注用户

	update:
		取消关注

	partial_update:
		取消关注
	"""
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
	serializer_class = FollowUserSerializers

	def get_queryset(self):
		return FollowUser.objects.filter(user=self.request.user)
