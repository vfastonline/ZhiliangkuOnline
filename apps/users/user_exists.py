# encoding: utf-8
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.mixins import RetrieveModelMixin

User = get_user_model()


class UserExistsSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("username", "mobile")


class UserExistsViewSet(RetrieveModelMixin, viewsets.GenericViewSet):
	"""
	read:
		手机号用户是否存在
	"""
	authentication_classes = ()
	permission_classes = ()
	queryset = User.objects.all()
	serializer_class = UserExistsSerializer
	lookup_field = "mobile"
