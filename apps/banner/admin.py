# encoding: utf-8
from django.contrib import admin

from .models import *


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
	list_display = ["name", "image", "category", "index"]
