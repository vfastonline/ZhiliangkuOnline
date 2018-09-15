# encoding: utf-8
import traceback

from django.apps import AppConfig
from django.db.models.signals import post_migrate


def init_banner(sender, verbosity, **kwargs):
	"""初始化-轮播图
	:param sender:
	:param kwargs:
	:return:
	"""
	try:
		from .models import Banner

		banners = [
			{"name": "首页0", "category": 1, "image": "banner/shouye_0.png", "index": 0, "desc": "描述信息"},
			{"name": "首页1", "category": 1, "image": "banner/shouye_1.png", "index": 1, "desc": "描述信息"},
			{"name": "首页2", "category": 1, "image": "banner/shouye_2.png", "index": 2, "desc": "描述信息"},
			{"name": "职业路径0", "category": 2, "image": "banner/zhiyelujing_0.png", "index": 0, "desc": "描述信息"},
			{"name": "职业路径1", "category": 2, "image": "banner/zhiyelujing_1.png", "index": 1, "desc": "描述信息"},
			{"name": "个人中心0", "category": 3, "image": "banner/gerenzhongxin_0.png", "index": 0, "desc": "描述信息"},
			{"name": "个人中心1", "category": 3, "image": "banner/gerenzhongxin_1.png", "index": 1, "desc": "描述信息"},

		]

		[Banner.objects.get_or_create(**banner) for banner in banners]

		if verbosity == 1:
			print("  - init 轮播图... OK")
	except:
		traceback.print_exc()


class BannerConfig(AppConfig):
	name = 'banner'
	verbose_name = "轮播图"
	main_menu_index = 0

	def ready(self):
		post_migrate.connect(init_banner, sender=self)
