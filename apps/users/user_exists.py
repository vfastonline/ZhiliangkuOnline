# encoding: utf-8
from rest_framework import viewsets, mixins

from .serializers import *


class UserExistsSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("username", "mobile")


class UserExistsViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	"""
	read:
		手机号用户是否存在

	"""
	queryset = User.objects.all()
	authentication_classes = ()
	permission_classes = ()
	lookup_field = "mobile"
	serializer_class = UserExistsSerializer
