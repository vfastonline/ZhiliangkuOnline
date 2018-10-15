from django.contrib import admin

from .models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ["_id", "project", "direction", "technical_labels", "image", "desc", "study", "course", "section",
					"stars", "hot", "new"]


@admin.register(CommonQuestion)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ["project", "question", "answer"]
