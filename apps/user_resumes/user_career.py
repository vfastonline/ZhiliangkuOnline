#!encoding:utf-8

from rest_framework import mixins, viewsets
from rest_framework import serializers
from rest_framework import status

from utils.drf_response_handler import JsonResponse
from .models import *


class UserResumeSerializer(serializers.ModelSerializer):
	"""
	用户简历'序列化
	"""
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = UserResume
		fields = ("_id",)


class CareerObjectiveSerializers(serializers.ModelSerializer):
	"""
	求职意向'序列化
	"""
	user_resume = UserResumeSerializer()

	class Meta:
		model = CareerObjective
		fields = ("user_resume", "position", "way_of_work", "city", "salary", "industry", "is_first")


class UserCareerViewSet(mixins.ListModelMixin,
						mixins.CreateModelMixin,
						viewsets.GenericViewSet):
	serializer_class = CareerObjectiveSerializers
	queryset = CareerObjective.objects.all()
	authentication_classes = ()
	permission_classes = ()
	lookup_field = "user_resume__user_id"

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(queryset, many=True)
		return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, desc="success")

	def create(self, request, *args, **kwargs):
		print("data", request.data)
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, desc="success")
