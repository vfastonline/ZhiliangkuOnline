#!encoding:utf-8

from rest_framework import mixins
from rest_framework import viewsets

from utils.exceptions import ResumeCategoryUnavailable
from .serializers import *


class UserResumeInformation(mixins.CreateModelMixin,
							mixins.UpdateModelMixin,
							mixins.DestroyModelMixin,
							viewsets.GenericViewSet, ):
	"""
	create:
	新增，求职意向，工作经历，项目经验，教育经历

	update:
	修改，求职意向，工作经历，项目经验，教育经历

	delete:
	删除，求职意向，工作经历，项目经验，教育经历

	"""
	authentication_classes = ()
	permission_classes = ()

	def get_resume_category(self):
		resume_category = self.kwargs.get("category")
		if not resume_category:
			raise ResumeCategoryUnavailable
		return resume_category

	def get_queryset(self):
		resume_category = self.get_resume_category()
		resume_category_model = {
			"CareerObjectives": CareerObjective,
			"WorkExperiences": WorkExperience,
			"ProjectExperiences": ProjectExperience,
			"EducationExperiences": EducationExperience,
		}
		resume_model = resume_category_model.get(resume_category)
		if not resume_model:
			raise ResumeCategoryUnavailable
		return resume_model.objects.filter(user_resume__user=self.request.user)

	def get_serializer_class(self):
		resume_category = self.get_resume_category()
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

			serializer = create_serializer.get(resume_category)
			if not serializer:
				raise ResumeCategoryUnavailable
			return serializer

		if self.action != 'create':
			serializer = other_serializer.get(resume_category)
			if not serializer:
				raise ResumeCategoryUnavailable
			return serializer
		return []
