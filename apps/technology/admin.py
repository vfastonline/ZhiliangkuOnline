from django.contrib import admin

from .models import *


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
	list_display = ["_id", "name", ]
