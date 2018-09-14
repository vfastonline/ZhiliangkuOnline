# encoding: utf-8
from rest_framework import serializers

from user_resumes.models import *


class EducationExperienceSerializer(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = EducationExperience
		fields = ("_id", "school", "discipline", "education", "start_time", "end_time", "experience")


class EducationExperienceCreateSerializer(serializers.ModelSerializer):
	user_resume_id = serializers.CharField()

	class Meta:
		model = EducationExperience
		fields = ("user_resume_id", "school", "discipline", "education", "start_time", "end_time", "experience")


class ProjectExperienceSerializer(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = ProjectExperience
		fields = ("_id", "name", "role", "url", "start_time", "end_time", "description", "performance")


class ProjectExperienceCreateSerializer(serializers.ModelSerializer):
	user_resume_id = serializers.CharField()

	class Meta:
		model = ProjectExperience
		fields = ("user_resume_id", "name", "role", "url", "start_time", "end_time", "description", "performance")


class WorkExperienceSerializer(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = WorkExperience
		fields = ("_id", "company", "position", "start_time", "end_time", "content")


class WorkExperienceCreateSerializer(serializers.ModelSerializer):
	user_resume_id = serializers.CharField()

	class Meta:
		model = WorkExperience
		fields = ("user_resume_id", "company", "position", "start_time", "end_time", "content")


class CareerObjectiveSerializer(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = CareerObjective
		fields = ("_id", "position", "way_of_work", "city", "salary", "industry", "is_first")


class CareerObjectiveCreateSerializer(serializers.ModelSerializer):
	user_resume_id = serializers.CharField()

	class Meta:
		model = CareerObjective
		fields = ("user_resume_id", "position", "way_of_work", "city", "salary", "industry", "is_first")
