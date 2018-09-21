# encoding: utf-8
from django.contrib import admin

from .models import *


@admin.register(DirectoryTree)
class BannerAdmin(admin.ModelAdmin):
	list_display = ["_id", "name", "category_type", "parent_category"]
	list_filter = ["category_type"]
