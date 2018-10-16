# encoding: utf-8
from itertools import chain

from django.contrib import admin

from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	list_display = ["_id", "video", "duration"]
	readonly_fields = ["duration", "vid", "data"]

	class Media:
		# js = ['js/webPlugins.js'] + tinymce_js + ["layer/layer.js"]
		js = ['webPlugins.js', 'jquery-3.3.1.min.js', 'layer/layer.js']
