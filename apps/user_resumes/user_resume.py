#!encoding:utf-8
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import *

User = get_user_model()


class UserResumeSerializer(serializers.ModelSerializer):
	"""
	用户简历'序列化
	"""
	_id = serializers.CharField(max_length=24)
	first_career_objective = serializers.SerializerMethodField()
	CareerObjectives = CareerObjectiveSerializer(many=True, read_only=True)
	WorkExperiences = WorkExperienceSerializer(many=True, read_only=True)
	ProjectExperiences = ProjectExperienceSerializer(many=True, read_only=True)
	EducationExperiences = EducationExperienceSerializer(many=True, read_only=True)

	@staticmethod
	def get_first_career_objective(obj):
		try:
			return obj.CareerObjectives.filter(is_first=True).first().position
		except:
			return ""

	class Meta:
		model = UserResume
		fields = (
			"_id", "name", "work_years", "education", "in_service_status", "current_company", "current_position",
			"advantage", "first_career_objective", "CareerObjectives",
			"WorkExperiences", "ProjectExperiences", "EducationExperiences")


class UserResumeUpdateSerializer(serializers.ModelSerializer):
	"""
	用户简历'修改'序列化
	"""
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = UserResume
		fields = (
			"_id", "name", "work_years", "education", "in_service_status", "current_company", "current_position",
			"advantage",)


class UserResumeViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
	"""
	list:
	获取用户基础简历信息

	update:
	更新用户基础简历信息，全量更新

	partial_update:
	更新用户基础简历信息，允许部分字段更新
	"""
	authentication_classes = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return UserResume.objects.filter(user=self.request.user)

	def get_serializer_class(self):
		if self.action == "list":
			return UserResumeSerializer
		else:
			return UserResumeUpdateSerializer
