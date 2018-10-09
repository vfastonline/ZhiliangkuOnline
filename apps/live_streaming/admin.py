#!encoding:utf-8
from django.contrib import admin

from live_streaming.models import Live


@admin.register(Live)
class LiveAdmin(admin.ModelAdmin):
	list_display = ('name', "channelId", "channelPasswd", "status", "autoPlay")
