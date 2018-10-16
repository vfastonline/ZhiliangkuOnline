# encoding: utf-8
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework import serializers

User = get_user_model()


class UserIsHasClassSerializers(serializers.Serializer):
	is_has_class = serializers.SerializerMethodField(read_only=True)

	def get_is_has_class(self, user):
		return user.team.exists()


class UserIsHasClassViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	"""
	read:
		用户是否归属于任意某个班级
	"""
	authentication_classes = ()
	permission_classes = ()
	queryset = User.objects.all()
	serializer_class = UserIsHasClassSerializers
