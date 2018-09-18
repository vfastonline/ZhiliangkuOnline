#!encoding:utf-8
from django.contrib import admin

from apps.medal.models import *


@admin.register(Medal)
class MedalAdmin(admin.ModelAdmin):
	list_display = ('name', "pathwel", "only")



@admin.register(UserMedal)
class UserMedalAdmin(admin.ModelAdmin):
	list_display = ('user', "medal", )
