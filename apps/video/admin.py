# encoding: utf-8
from django.contrib import admin

from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	list_display = ["_id", "video_name"]

	def video_name(self, obj):
		return obj.video.name if obj.video else ""
