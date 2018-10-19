# encoding: utf-8

from django.contrib import admin

from .models import *


@admin.register(ScoreItem)
class ScoreItemAdmin(admin.ModelAdmin):
	list_display = ["role", "name", "desc"]


@admin.register(UserScore)
class UserScoreAdmin(admin.ModelAdmin):
	list_display = ["users", "feedback", "self_evaluation", "owners", "created_at"]

	def users(self, obj):
		return obj.user.username

	def owners(self, obj):
		return obj.owner.username

	users.short_description = "用户"
	owners.short_description = "评分人"
