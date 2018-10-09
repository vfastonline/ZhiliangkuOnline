#!encoding:utf-8
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from djongo import models

from utils.model import BaseModelMixin

User = get_user_model()


class Medal(BaseModelMixin):
	"""
	勋章
	"""

	name = models.CharField('名称', max_length=50)
	image = models.ImageField('图片', upload_to='medal')
	only = models.CharField('系统识别名称', max_length=50, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "勋章"
		verbose_name_plural = verbose_name


class UserMedal(BaseModelMixin):
	"""用户勋章 """

	user = models.ForeignKey(User, verbose_name="用户", related_name='UserMedals', on_delete=models.CASCADE)
	medal = models.ForeignKey(Medal, verbose_name="获得的勋章", on_delete=models.CASCADE, blank=True)

	def __str__(self):
		return self.user.name

	class Meta:
		verbose_name = "用户勋章"
		verbose_name_plural = verbose_name
