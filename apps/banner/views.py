# encoding: utf-8
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import viewsets

from .serializers import *


class BannerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
	Return a list of all the existing users.
	"""
	queryset = Banner.objects.all()
	serializer_class = BannerSerializer
	authentication_classes = ()
	permission_classes = ()

	# 常用过滤器之DjangoFilterBackend, SearchFilter, OrderingFilter
	filter_backends = (DjangoFilterBackend,)

	filter_fields = ("category",)
	ordering = ('index',)
