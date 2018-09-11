# encoding: utf-8
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets

from utils.drf_response_handler import JsonResponse
from .serializers import *


class BannerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	轮播图
	"""
	authentication_classes = ()
	permission_classes = ()
	queryset = Banner.objects.all()
	serializer_class = BannerSerializer

	# 常用过滤器之DjangoFilterBackend, SearchFilter, OrderingFilter
	filter_backends = (DjangoFilterBackend, filters.OrderingFilter)

	filter_fields = ('category',)
	ordering = ('index',)

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(queryset, many=True)
		return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, desc="success")
