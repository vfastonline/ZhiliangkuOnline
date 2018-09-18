from django.contrib import admin

from apps.record.models import WatchRecord


@admin.register(WatchRecord)
class WatchRecordAdmin(admin.ModelAdmin):
	list_display = ('user', "video", 'course', 'video_process',
					'duration', "total_duration", 'status', 'create_time'
					)
