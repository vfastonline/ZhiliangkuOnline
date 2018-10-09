#!encoding:utf-8
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from djongo import models

User = get_user_model()

from utils.model import BaseModelMixin


class Notification(BaseModelMixin):
	"""消息通知
	- `custom_user`: 消息所有人的用户
	- `title`: 消息标题
	- `content`: 消息内容
	- `create_time`: 消息创建时间
	- `have_read`: 消息是否已读
	"""

	user = models.ForeignKey(User, verbose_name="用户", related_name='NotificationCustomUser', db_index=True,
							 on_delete=models.CASCADE)
	title = models.CharField('标题', max_length=255, default="", db_index=True)
	content = models.TextField('内容', max_length=255, default="")
	have_read = models.BooleanField("已读", default=False)

	def __str__(self):
		return '<Notification %s: %s>' % (self.user.username, self.title)

	class Meta:
		verbose_name = "消息通知"
		verbose_name_plural = verbose_name


class UserNotificationsCount(BaseModelMixin):
	"""用户的未读消息数目
	- `custom_user`: 消息所有人的用户
	- `have_read`: 消息未读个数
	"""

	user = models.ForeignKey(User, verbose_name="用户", db_index=True, on_delete=models.CASCADE)
	unread_count = models.IntegerField("未读消息数", default=0)

	def __str__(self):
		return '<UserNotificationsCount %s: %s>' % (self.user.username, self.unread_count)

	class Meta:
		verbose_name = "用户未读消息"
		verbose_name_plural = verbose_name
