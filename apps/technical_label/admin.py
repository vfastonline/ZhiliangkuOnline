from django.contrib import admin

from .models import *


@admin.register(TechnicalLabel)
class TechnicalLabelAdmin(admin.ModelAdmin):
	list_display = ["_id", "name", ]
