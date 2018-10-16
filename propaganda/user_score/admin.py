# encoding: utf-8

from django.contrib import admin

from .models import *


@admin.register(ScoreItem)
class ScoreItemAdmin(admin.ModelAdmin):
	list_display = ["role", "name", "desc"]


@admin.register(UserScore)
class UserScoreAdmin(admin.ModelAdmin):
	list_display = ["user", "feedback"]
