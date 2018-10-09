#!encoding:utf-8
from django.contrib import admin

from notification.models import *


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
	list_display = ('user', "title", "content", "have_read")


@admin.register(UserNotificationsCount)
class UserNotificationsCountAdmin(admin.ModelAdmin):
	list_display = ('user', "unread")
