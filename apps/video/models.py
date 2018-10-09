#!encoding:utf-8
from __future__ import unicode_literals

from djongo import models

from directory_tree.models import DirectoryTree
from utils.model import BaseModelMixin


class Video(BaseModelMixin):
	"""
	视频
	"""
	video = models.ForeignKey(DirectoryTree, verbose_name='视频', related_name='videos', blank=True, null=True,
							  on_delete=models.SET_NULL, limit_choices_to={'category_type': "video"})
	notes = models.TextField('讲师笔记', blank=True)
	vid = models.CharField("vid", max_length=255, blank=True)
	datas = models.TextField("保利威视视频信息", blank=True)

	class Meta:
		verbose_name = "视频"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.video.name
