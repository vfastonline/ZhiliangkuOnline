# encoding: utf-8

from django.contrib import admin

from .models import *


@admin.register(UserResume)
class UserResumeAdmin(admin.ModelAdmin):
	list_display = ['user', 'name', 'work_years']


@admin.register(CareerObjective)
class CareerObjectiveAdmin(admin.ModelAdmin):
	list_display = ['user_resume', 'position', 'way_of_work', 'city']


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
	list_display = ['user_resume', 'company', 'position']


@admin.register(ProjectExperience)
class ProjectExperienceAdmin(admin.ModelAdmin):
	list_display = ['name', 'role', 'url']


@admin.register(EducationExperience)
class EducationExperienceAdmin(admin.ModelAdmin):
	list_display = ['school', 'discipline', 'education']
