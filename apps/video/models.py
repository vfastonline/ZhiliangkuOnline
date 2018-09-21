from django.db import models

from directory_tree.models import DirectoryTree
from utils.model import BaseModelMixin


class Video(BaseModelMixin):
	"""
	视频
	"""
	video = models.ForeignKey(DirectoryTree, verbose_name='视频', related_name='video', blank=True, null=True,
							  on_delete=models.SET_NULL, limit_choices_to={'category_type': "video"})
	vid = models.CharField("vid", max_length=255, blank=True)
	data = models.TextField("视频信息", blank=True)

	class Meta:
		verbose_name = "视频"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.video.name
