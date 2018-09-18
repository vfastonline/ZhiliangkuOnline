#!encoding:utf-8
from __future__ import unicode_literals

from colorfield.fields import ColorField
from django.db import models

from utils.model import BaseModelMixin


class Live(BaseModelMixin):
	"""直播"""

	AUTOPLAY = (
		(0, '否'),
		(1, '是'),
	)
	STATUS = (
		("live", '正在直播'),
		("end", '直播结束'),
	)
	name = models.CharField('频道名称', max_length=50, unique=True)
	channelId = models.IntegerField('频道号', blank=True)
	channelPasswd = models.CharField('频道密码', max_length=50, default="111111", blank=True)
	playerColor = ColorField('播放器控制栏颜色', max_length=50, default="#666666", blank=True)
	autoPlay = models.IntegerField('是否自动播放', choices=AUTOPLAY, default=1)  # 是否自动播放，0/1，默认1
	pathwel = models.ImageField('直播图片', upload_to='live/%Y%m%d', )
	status = models.CharField('状态', max_length=5, choices=STATUS, default='end')  # 频道的直播状态，字符串，值包括：live end
	data = models.TextField("创建直播接口返回值", blank=True)
	desc = models.TextField('简介', max_length=1000, default='', blank=True,)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "直播间"
		verbose_name_plural = verbose_name
		ordering = ['name']
