#!encoding:utf-8

from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from utils.drf_response_handler import JsonResponse
from utils.exceptions import ResumeCategoryUnavailable
from .serializers import *


class UserResumeInformation(mixins.CreateModelMixin,
							mixins.UpdateModelMixin,
							mixins.DestroyModelMixin,
							viewsets.GenericViewSet, ):
	"""
	用户简历-子信息增删改
	"""
	authentication_classes = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		param = self.request.query_params
		category = param.get("category")
		param_model = {
			"CareerObjectives": CareerObjective,
			"WorkExperiences": WorkExperience,
			"ProjectExperiences": ProjectExperience,
			"EducationExperiences": EducationExperience,
		}
		get_model = param_model.get(category)
		if not get_model:
			raise ResumeCategoryUnavailable
		return get_model.objects.filter(user_resume__user=self.request.user)

	def get_serializer_class(self):
		param = self.request.query_params
		category = param.get("category")  # 简历子数据类型，求职意向等
		create_serializer = {
			"CareerObjectives": CareerObjectiveCreateSerializer,
			"WorkExperiences": WorkExperienceCreateSerializer,
			"ProjectExperiences": ProjectExperienceCreateSerializer,
			"EducationExperiences": EducationExperienceCreateSerializer,
		}
		other_serializer = {
			"CareerObjectives": CareerObjectiveSerializer,
			"WorkExperiences": WorkExperienceSerializer,
			"ProjectExperiences": ProjectExperienceSerializer,
			"EducationExperiences": EducationExperienceSerializer,
		}

		if self.action == 'create':

			serializer = create_serializer.get(category)
			if not serializer:
				raise ResumeCategoryUnavailable
			return serializer

		if self.action != 'create':
			serializer = other_serializer.get(category)
			if not serializer:
				raise ResumeCategoryUnavailable
			return serializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, desc="success")

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		self.perform_destroy(instance)
		return JsonResponse(code=status.HTTP_200_OK, desc="success")

	def update(self, request, *args, **kwargs):
		partial = kwargs.pop('partial', False)
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, desc="success")
