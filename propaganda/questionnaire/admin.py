from django.contrib import admin

from .models import *


@admin.register(QuestionnaireScore)
class QuestionnaireScoreAdmin(admin.ModelAdmin):
	list_display = ["user", "category", "value"]


@admin.register(EQ)
class EQAdmin(admin.ModelAdmin):
	list_display = ["title"]


@admin.register(IQ)
class IQAdmin(admin.ModelAdmin):
	list_display = ["title"]
