# encoding: utf8
import csv
import os
import traceback

from django.apps import AppConfig
from django.core.mail import send_mail
from django.db.models.signals import post_migrate, post_save

from ZhiliangkuOnline.settings import EMAIL_HOST_USER


def init_eq(sender, verbosity, **kwargs):
	"""初始化-EQ测试题
	:param sender:
	:param kwargs:
	:return:
	"""
	try:
		from .models import EQ
		from .models import Option

		csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "EQ_file.csv")

		csv_reader = csv.reader(open(csv_file))
		for index, row in enumerate(csv_reader):
			if index == 0:
				continue

			add_data = {
				"title": row[2],
			}

			options = list()
			for option in eval(row[1]):
				options.append(Option(**option))
			add_data.update({"option": options})

			eq_obj = EQ.objects.filter(title=row[2])
			if not eq_obj.exists():
				EQ.objects.create(**add_data)

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
		from .models import Option

		csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "IQ_file.csv")

		csv_reader = csv.reader(open(csv_file))
		for index, row in enumerate(csv_reader):
			if index == 0:
				continue

			add_data = {
				"title": row[3],
			}

			if row[1]:
				image = row[1].split("/")[-1]
				add_data.update({"image": "/".join(["iq_image", image])})

			options = list()
			for option in eval(row[2]):
				options.append(Option(**option))
			add_data.update({"option": options})

			iq_obj = IQ.objects.filter(title=row[3])
			if not iq_obj.exists():
				IQ.objects.create(**add_data)

		if verbosity == 1:
			print("  - init IQ测试题... OK")
	except:
		traceback.print_exc()


def question_nairescore_post_save(sender, instance=None, created=False, **kwargs):
	"""发送用户问卷成绩到咨询师邮箱
	:param sender:
	:param instance:
	:param created:
	:param kwargs:
	:return:
	"""
	if created:
		subject = "智量酷-问卷调查"
		content = "姓名：{name} \n手机号：{phone} \n问卷类型：{category} \n成绩：{value} "
		message = content.format(name=instance.user.name,
								 phone=instance.user.mobile,
								 category=instance.get_category_display(),
								 value=instance.value)
		send_mail(subject, message, EMAIL_HOST_USER, [instance.consultant_email, ])


class QuestionnaireConfig(AppConfig):
	name = 'questionnaire'
	verbose_name = "问卷调查"
	main_menu_index = 22

	def ready(self):
		post_migrate.connect(init_iq, sender=self)
		post_migrate.connect(init_eq, sender=self)
		from .models import QuestionnaireScore
		post_save.connect(question_nairescore_post_save, sender=QuestionnaireScore)
