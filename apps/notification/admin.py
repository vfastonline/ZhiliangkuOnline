#!encoding:utf-8
from django.contrib import admin

from apps.notification.models import *


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
	list_display = ('user', "title", "content", "have_read")


@admin.register(UserNotificationsCount)
class UserNotificationsCountAdmin(admin.ModelAdmin):
	list_display = ('user', "unread_count")
