# encoding: utf-8
import json

from bson import ObjectId
from django.apps import apps
from django.contrib import admin
from django.utils.text import capfirst
from rest_framework.routers import DefaultRouter

router = DefaultRouter()  # 定义基础router，其他模块引用后注册接口

# 手机号码'正则表达式
REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"


# 重写json解码，适应mongodb，ObjectId
class JSONEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, ObjectId):
			return str(o)
		return json.JSONEncoder.default(self, o)


# 猴子补丁，扩展json解码
def monkey_patch_jsonencoder():
	json.JSONEncoder = JSONEncoder


monkey_patch_jsonencoder()


# 查找app顺序
def find_app_index(app_label):
	app = apps.get_app_config(app_label)
	main_menu_index = getattr(app, 'main_menu_index', 9999)
	return main_menu_index


# 查找模型索引
def find_model_index(name):
	count = 0
	for model, model_admin in admin.site._registry.items():
		if capfirst(model._meta.verbose_name_plural) == name:
			return count
		else:
			count += 1
	return count


# 顺序
def index_decorator(func):
	def inner(*args, **kwargs):
		templateresponse = func(*args, **kwargs)
		app_list = templateresponse.context_data['app_list']
		app_list.sort(key=lambda r: find_app_index(r['app_label']))
		for app in app_list:
			app['models'].sort(key=lambda x: find_model_index(x['name']))
		return templateresponse

	return inner
