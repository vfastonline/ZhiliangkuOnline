# encoding: utf-8

from django.contrib import admin

from .models import *


@admin.register(UserResume)
class UserResumeAdmin(admin.ModelAdmin):
	list_display = ['user', 'name', 'work_years']


@admin.register(CareerObjective)
class CareerObjectiveAdmin(admin.ModelAdmin):
	list_display = ['position', 'way_of_work', 'city']
