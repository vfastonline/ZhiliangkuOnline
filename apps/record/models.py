#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models

from tracks_learning.models import Video, Course
from users.models import UserProfile
from utils.model import BaseModelMixin


class WatchRecord(BaseModelMixin):
	"""用户观看记录表"""
	STATUS = (
		(1, '已看完'),
		(0, '未看完')
	)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
	video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True, verbose_name='视频')
	course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
	video_process = models.IntegerField('观看时间', default=0, help_text="秒")
	duration = models.IntegerField('时长', default=0, help_text="单位：秒")
	total_duration = models.IntegerField('累计观看时长', default=0, blank=True)
	status = models.IntegerField('观看状态', choices=STATUS, default=0)
	create_time = models.DateTimeField(verbose_name='记录时间', auto_now=True)

	def __str__(self):
		return self.user.name + "|" + self.course.name

	class Meta:
		verbose_name = "学生观看视频记录"
		verbose_name_plural = verbose_name
