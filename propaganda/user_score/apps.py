# encoding: utf-8
import traceback

from django.apps import AppConfig
from django.db.models.signals import post_migrate


def init_score_item(sender, verbosity, **kwargs):
	"""
	初始化，用户评分，得分项
	:param sender:
	:param kwargs:
	:return:
	"""
	try:
		from .models import ScoreItem

		score_items = [
			{"name": "精神面貌", "desc": "xx", "role": "2"},
			{"name": "课堂气氛", "desc": "xx", "role": "2"},
			{"name": "知识引导", "desc": "xx", "role": "2"},
			{"name": "理解程度", "desc": "xx", "role": "1"},
			{"name": "操作程度", "desc": "xx", "role": "1"},
		]

		[ScoreItem.objects.get_or_create(**score_item) for score_item in score_items]

		if verbosity == 1:
			print(" 初始化-用户评分-得分项 OK")
	except:
		traceback.print_exc()


class UserScoreConfig(AppConfig):
	name = 'user_score'
	verbose_name = "用户评分"
	main_menu_index = 23

	def ready(self):
		post_migrate.connect(init_score_item, sender=self)
