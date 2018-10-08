# encoding: utf-8
import traceback

from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate, post_save


def init_role(sender, verbosity, **kwargs):
	"""初始化-角色信息
	:param sender:
	:param kwargs:
	:return:
	"""
	try:
		from .models import Role
		roles = {0: '学生', 1: "老师", 2: "HR", 3: "其他", 4: "咨询师"}
		[Role.objects.get_or_create(**{"index": index, "name": name}) for index, name in roles.items()]
		if verbosity == 1:
			print("  - init 用户角色... OK")
	except:
		traceback.print_exc()


def user_post_save(sender, instance=None, created=False, **kwargs):
	"""用户信息保存后，设置学生角色，添加用户基础信息
	:param sender:
	:param instance:
	:param created:
	:param kwargs:
	:return:
	"""
	from user_resumes.models import UserResume
	from users.models import Role
	if created:
		instance.role.add(Role.objects.get(index=0))
		instance.save()
		UserResume.objects.get_or_create(user=instance)


class UsersConfig(AppConfig):
	name = 'users'
	verbose_name = "用户管理"
	main_menu_index = 1

	def ready(self):
		post_migrate.connect(init_role, sender=self)
		user = get_user_model()
		post_save.connect(user_post_save, sender=user)
