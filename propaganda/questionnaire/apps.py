# encoding: utf8
import csv
import os
import traceback

from django.apps import AppConfig
from django.db.models.signals import post_migrate


def init_eq(sender, verbosity, **kwargs):
	"""初始化-EQ测试题
	:param sender:
	:param kwargs:
	:return:
	"""
	try:
		from .models import EQ
		csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "EQ_file.csv")

		csv_reader = csv.reader(open(csv_file))
		for index, row in enumerate(csv_reader):
			if index == 0:
				continue
			EQ.objects.get_or_create(title=row[2], option=eval(row[1]))

		if verbosity == 1:
			print("  - init EQ测试题... OK")
	except:
		traceback.print_exc()


def init_iq(sender, verbosity, **kwargs):
	"""初始化-IQ测试题
	:param sender:
	:param kwargs:
	:return:
	"""
	try:
		from .models import IQ
		csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "iQ_file.csv")

		csv_reader = csv.reader(open(csv_file))
		for index, row in enumerate(csv_reader):
			if index == 0:
				continue

			add_data = {
				"title": row[3],
				"option": eval(row[2]),
				"image": "",
			}
			if row[1]:
				image = row[1].split("/")[-1]
				add_data.update({"image": "/".join(["iq_image", image])})
			IQ.objects.get_or_create(**add_data)

		if verbosity == 1:
			print("  - init IQ测试题... OK")
	except:
		traceback.print_exc()


class QuestionnaireConfig(AppConfig):
	name = 'questionnaire'
	verbose_name = "问卷调查"

	def ready(self):
		post_migrate.connect(init_iq, sender=self)
		post_migrate.connect(init_eq, sender=self)
