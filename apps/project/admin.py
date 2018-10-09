from django.contrib import admin

from .models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ["_id", "project", ]


@admin.register(CommonQuestion)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ["project", "question", "answer"]
