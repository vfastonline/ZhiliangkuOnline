# encoding: utf-8
from django.contrib import admin

from .models import PracticeRecord


@admin.register(PracticeRecord)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ("user", 'video', "times", "is_pass")

