#!encoding:utf-8
import traceback

from django.apps import AppConfig
from django.db.models.signals import post_migrate


def init_technical_label(sender, verbosity, **kwargs):
	"""
	初始化-技术标签
	:param sender:
	:param verbosity:
	:param kwargs:
	:return:
	"""
	from .models import TechnicalLabel
	try:
		technical_label = [
			{"name": "Html/CSS"},
			{"name": "JavaScript"},
			{"name": "AngularJS"}
		]
		[TechnicalLabel.objects.get_or_create(**technical) for technical in technical_label]
		if verbosity == 1:
			print("初始化-技术标签 OK")
	except:
		traceback.print_exc()


class TechnicalLabelConfig(AppConfig):
	name = 'technical_label'
	verbose_name = "技术标签"
	main_menu_index = 14

	def ready(self):
		post_migrate.connect(init_technical_label, sender=self)
