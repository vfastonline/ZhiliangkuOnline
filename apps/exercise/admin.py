#!encoding:utf-8

from django.contrib import admin

from exercise.models import *
from user_operation.models import PracticeRecord


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ("video", 'title', "right_answer", "detail")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
	list_display = ("question", 'option', "content")


@admin.register(PracticeRecord)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ("user", 'video', "times", "is_pass")
