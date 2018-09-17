# encoding: utf-8
import traceback

from django.apps import AppConfig
from django.db.models.signals import post_migrate


def init_user_profile_role(sender, verbosity, **kwargs):
	"""初始化-用户角色信息
	:param sender:
	:param kwargs:
	:return:
	"""
	try:
		from .models import Role
		roles = {0: '学生', 1: "老师", 2: "HR", 3: "其他"}
		[Role.objects.get_or_create(**{"index": index, "name": name}) for index, name in roles.items()]
		if verbosity == 1:
			print("  - init 用户角色... OK")
	except:
		traceback.print_exc()


class UsersConfig(AppConfig):
	name = 'users'
	verbose_name = "用户管理"
	main_menu_index = 1

	def ready(self):
		post_migrate.connect(init_user_profile_role, sender=self)
