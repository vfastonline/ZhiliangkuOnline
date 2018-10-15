#!encoding:utf-8
import traceback

from django.apps import AppConfig
from django.db.models.signals import post_migrate


def init_direction(sender, verbosity, **kwargs):
	"""
	初始化-项目方向
	:param sender:
	:param verbosity:
	:param kwargs:
	:return:
	"""
	from .models import DirectoryTree
	try:
		directions = [
			{"category": "direction", "name": "MYSQL"},
			{"category": "direction", "name": "大数据"},
			{"category": "direction", "name": "爬虫"},
			{"category": "direction", "name": "AI"},
		]

		[DirectoryTree.objects.get_or_create(**direction) for direction in directions]
		if verbosity == 1:
			print("初始化-项目方向 OK")
	except:
		traceback.print_exc()


class DataStructureConfig(AppConfig):
	name = 'directory_tree'
	verbose_name = "目录树"

	def ready(self):
		post_migrate.connect(init_direction, sender=self)
