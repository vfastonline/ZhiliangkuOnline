#!encoding:utf-8
from __future__ import unicode_literals

from utils.model import *
from video.models import Video


class Answer(models.Model):
	"""
	选项
	"""
	RIGHTANSWER = (
		("1", "A"),
		("2", "B"),
		("3", "C"),
		("4", "D"),
	)
	option = models.CharField('选项', max_length=1, choices=RIGHTANSWER)
	content = models.TextField('内容', max_length=255, default="")

	def __str__(self):
		return self.content

	class Meta:
		abstract = True


class Question(BaseModelMixin):
	"""
	问题
	"""
	RIGHT = (
		("1", "A"),
		("2", "B"),
		("3", "C"),
		("4", "D"),
	)
	video = models.ForeignKey(Video, verbose_name='所属视频', related_name='Questions', on_delete=models.CASCADE)
	title = models.CharField('标题', max_length=255)
	right = models.CharField('正确答案', max_length=1, choices=RIGHT)
	answer = models.ArrayModelField(
		model_container=Answer,
	)
	detail = models.TextField('习题详解', max_length=255, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "习题"
		verbose_name_plural = "习题"
		ordering = ["video"]
		index_together = ["video"]
