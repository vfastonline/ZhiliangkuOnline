# encoding: utf-8
import traceback

from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate, post_save

User = get_user_model()


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


def post_save_user(sender, instance=None, created=False, **kwargs):
	# 是否新建，因为update的时候也会进行post_save
	from user_resumes.models import UserResume
	from users.models import Role
	if created:
		# 第三方接口创建用户后，增加默认学生角色，创建默认简历
		instance.roles.add(Role.objects.get(index=0))
		instance.save()
		UserResume.objects.create(user=instance)


class UsersConfig(AppConfig):
	name = 'users'
	verbose_name = "用户管理"
	main_menu_index = 1

	def ready(self):
		post_migrate.connect(init_user_profile_role, sender=self)
		post_save.connect(post_save_user, sender=User)
