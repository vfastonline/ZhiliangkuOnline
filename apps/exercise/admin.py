#!encoding:utf-8

from django.contrib import admin

from exercise.models import *


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ("video", 'title', "right")
