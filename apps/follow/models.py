#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models

from users.models import UserProfile
from utils.model import BaseModelMixin


class Userfollow(BaseModelMixin):
	"""用户关注 """

	user = models.ForeignKey(UserProfile, verbose_name="用户", related_name='UserProfile',
							 on_delete=models.CASCADE)
	user_follow = models.ForeignKey(UserProfile, verbose_name="被关注用户", related_name='ToUserProfile',
									on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

	class Meta:
		unique_together = ('user', 'user_follow',)
		verbose_name = "用户关注"
		verbose_name_plural = verbose_name
