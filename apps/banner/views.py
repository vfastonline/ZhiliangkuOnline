# encoding: utf-8
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets

from banner.serializers import *
from utils.drf_response_handler import JsonResponse


class SchoolFilter(django_filters.FilterSet):
	class Meta:
		model = Banner
		fields = ['category']


class BannerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
	Return a list of all the existing users.
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
