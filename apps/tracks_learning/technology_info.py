#!encoding:utf-8

from rest_framework import serializers
from rest_framework import status
from rest_framework import viewsets, mixins

from tracks_learning.models import *
from utils.drf_response_handler import JsonResponse


class TechnologySerializer(serializers.ModelSerializer):
	video_id=serializers.CharField()
	class Meta:
		model = Technology
		fields = ("name","desc","video_id")



class TechnologyListInfo(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	技术分类列表信息
	"""
	authentication_classes = ()
	permission_classes = ()

	queryset = Technology.objects.all()
	serializer_class = TechnologySerializer

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(queryset, many=True)
		return JsonResponse(serializer.data, code=status.HTTP_200_OK, desc="success")
