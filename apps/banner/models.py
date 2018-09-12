# encoding: utf8
from utils.model import *


class Banner(BaseModelMixin):
	"""
	轮播图
	"""
	CATEGORY = (
		("1", "首页"),
		("2", "职业路径"),
		("3", "个人中心"),
	)

	name = models.CharField('轮播名称', max_length=50)
	image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
	category = models.CharField('类别', max_length=1, choices=CATEGORY, db_index=True)
	index = models.IntegerField(default=0, verbose_name="轮播顺序", db_index=True)
	desc = models.TextField(default="", verbose_name="轮播描述", help_text="轮播描述")

	class Meta:
		verbose_name = '轮播图'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name
