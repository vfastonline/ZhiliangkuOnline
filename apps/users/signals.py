# encoding: utf-8

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


# # 参数一接收哪种信号，参数二是接收哪个model的信号
# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
# 	# 是否新建，因为update的时候也会进行post_save
# 	if created:
# 		print(11111111111111, instance, instance._id)
# 		instance.id = str(instance._id)
# 		instance.save()
