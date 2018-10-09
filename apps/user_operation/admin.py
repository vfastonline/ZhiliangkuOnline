# encoding: utf-8
from django.contrib import admin

from .models import *


@admin.register(PracticeRecord)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ("user", 'video', "times", "is_pass")


@admin.register(Notes)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ("user", 'video', "title", "approve", "oppose")


@admin.register(FollowUser)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ("user", "follow")


@admin.register(WishList)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ("user", "project")


@admin.register(ParticipateProject)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ("user", "project")


@admin.register(LearnCourse)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ("user", "course")


@admin.register(VideoWatchRecord)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ("user", "video", "moment", "duration", "complete")


@admin.register(FavVideo)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ("user", "video")


@admin.register(AssessmentRecord)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ("user", "assessment", "is_pass", "times")


@admin.register(GoldRecord)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ("user", "get_way", "total")


@admin.register(ProjectLearnRate)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ("user", "project", "rate")


@admin.register(ProjectAppraisal)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ("user", "project", "star", "desc")
