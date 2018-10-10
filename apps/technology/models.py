#!encoding:utf-8
from djongo import models

from utils.model import BaseModelMixin


class Technology(BaseModelMixin):
	"""
	技术标签
	"""
	name = models.CharField('名称', max_length=155)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "技术标签"
		verbose_name_plural = verbose_name
