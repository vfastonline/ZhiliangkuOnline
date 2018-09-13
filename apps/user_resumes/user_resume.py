#!encoding:utf-8
from rest_framework import mixins, viewsets
from rest_framework import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from utils.drf_response_handler import JsonResponse
from .models import *

User = get_user_model()


class EducationExperienceSerializer(serializers.ModelSerializer):
	class Meta:
		model = EducationExperience
		fields = ("school", "discipline", "education", "start_time", "end_time")


class ProjectExperienceSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProjectExperience
		fields = ("name", "role", "url", "start_time", "end_time")


class WorkExperienceSerializer(serializers.ModelSerializer):
	class Meta:
		model = WorkExperience
		fields = ("company", "position", "start_time", "end_time")


class CareerObjectiveSerializer(serializers.ModelSerializer):
	class Meta:
		model = CareerObjective
		fields = ("position", "city", "salary", "industry", "is_first")


class UserResumeSerializer(serializers.ModelSerializer):
	"""
	用户简历'序列化
	"""
	_id = serializers.CharField(max_length=24)
	CareerObjectives = CareerObjectiveSerializer(many=True, read_only=True)
	WorkExperiences = WorkExperienceSerializer(many=True, read_only=True)
	ProjectExperiences = ProjectExperienceSerializer(many=True, read_only=True)
	EducationExperiences = EducationExperienceSerializer(many=True, read_only=True)

	class Meta:
		model = UserResume
		fields = (
			"_id", "name", "work_years", "education", "in_service_status", "current_company", "current_position",
			"advantage", "CareerObjectives",
			"WorkExperiences", "ProjectExperiences", "EducationExperiences")


class UserResumeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	用户，简历信息
	"""
	authentication_classes = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	serializer_class = UserResumeSerializer

	def get_queryset(self):
		return UserResume.objects.filter(user=self.request.user)

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(queryset, many=True)
		return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, desc="success")
