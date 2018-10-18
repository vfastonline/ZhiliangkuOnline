# encoding: utf-8

from django.contrib import admin
from django.utils.html import format_html

from .models import *


@admin.register(ScoreItem)
class ScoreItemAdmin(admin.ModelAdmin):
	list_display = ["role", "name", "desc"]


@admin.register(UserScore)
class UserScoreAdmin(admin.ModelAdmin):
	list_display = ["users", "feedback", "owners", "self_evaluation"]

	def users(self, obj):
		return obj.user.username

	def owners(self, obj):
		return obj.owner.username

	def self_evaluation(self, obj):
		icon = "icon-no.svg"
		if obj.user == obj.owner:
			icon = "icon-yes.svg"
		return format_html('<img src="/static/admin/img/%s" alt="True">' % icon)

	users.short_description = "用户"
	owners.short_description = "评分人"
	self_evaluation.short_description = "自评"
