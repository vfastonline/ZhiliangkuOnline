#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models

from users.models import UserProfile
from utils.model import BaseModelMixin


class Medal(BaseModelMixin):
	"""勋章"""
	name = models.CharField('名称', max_length=50)
	pathwel = models.ImageField('图片', upload_to='medal', )  # storage=ImageStorage()
	only = models.CharField('系统识别名称', max_length=50, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "勋章"
		verbose_name_plural = verbose_name


class UserMedal(BaseModelMixin):
	"""用户勋章 """

	user = models.ForeignKey(UserProfile, verbose_name="用户", related_name='UserMedals',
							 on_delete=models.CASCADE)
	medal = models.ForeignKey(Medal, verbose_name="获得的勋章", on_delete=models.CASCADE, blank=True)


	def __str__(self):
		return self.user.name

	class Meta:
		verbose_name = "用户勋章"
		verbose_name_plural = verbose_name
