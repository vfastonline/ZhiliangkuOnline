#!encoding:utf-8
from django.contrib import admin

from medal.models import *


@admin.register(Medal)
class MedalAdmin(admin.ModelAdmin):
	list_display = ('name', "image", "only")


@admin.register(UserMedal)
class UserMedalAdmin(admin.ModelAdmin):
	list_display = ('user', 'medals')
