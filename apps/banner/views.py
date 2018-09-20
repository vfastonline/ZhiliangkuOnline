# encoding: utf-8
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import *


class BannerViewSet(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取banner信息
	"""
	queryset = Banner.objects.all()
	serializer_class = BannerSerializer
	authentication_classes = ()
	permission_classes = ()

	filter_backends = (DjangoFilterBackend,)

	filter_fields = ("category",)
	ordering = ('index',)
