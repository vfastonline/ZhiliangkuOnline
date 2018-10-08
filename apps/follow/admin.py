#!encoding:utf-8
from django.contrib import admin

from follow.models import *


@admin.register(Userfollow)
class UserMedalAdmin(admin.ModelAdmin):
	list_display = ('_id', 'user', "user_follow_id",)
