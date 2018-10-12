# encoding: utf-8
from django.contrib import admin

from .models import *


@admin.register(PracticeRecord)
class PracticeRecordAdmin(admin.ModelAdmin):
	list_display = ("user", 'video', "times", "is_pass")


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
	list_display = ("user", 'video', "title", "approve", "oppose", "reprint_count", "is_show")


@admin.register(FollowUser)
class FollowUserAdmin(admin.ModelAdmin):
	list_display = ("user", "follow")


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
	list_display = ("user", "project")


@admin.register(ParticipateProject)
class UParticipateProjectAdmin(admin.ModelAdmin):
	list_display = ("user", "project")


@admin.register(LearnCourse)
class LearnCourseAdmin(admin.ModelAdmin):
	list_display = ("user", "course")


@admin.register(VideoWatchRecord)
class VideoWatchRecordAdmin(admin.ModelAdmin):
	list_display = ("user", "video", "moment", "duration", "complete")


@admin.register(FavVideo)
class FavVideoAdmin(admin.ModelAdmin):
	list_display = ("user", "video")


@admin.register(AssessmentRecord)
class AssessmentRecordAdmin(admin.ModelAdmin):
	list_display = ("user", "assessment", "is_pass", "times")


@admin.register(GoldRecord)
class GoldRecordAdmin(admin.ModelAdmin):
	list_display = ("user", "get_way", "total")


@admin.register(ProjectLearnRate)
class ProjectLearnRateAdmin(admin.ModelAdmin):
	list_display = ("user", "project", "rate")


@admin.register(ProjectAppraisal)
class ProjectAppraisalAdmin(admin.ModelAdmin):
	list_display = ("user", "project", "star", "desc")


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
	list_display = ("user", "reason", "source", "types")
