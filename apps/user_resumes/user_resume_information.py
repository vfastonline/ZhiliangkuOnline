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
		category = self.request.query_params.get("category","")  # 简历子数据类型，求职意向等
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

