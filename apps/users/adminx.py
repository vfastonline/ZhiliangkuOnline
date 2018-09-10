# encoding: utf-8

import xadmin
from xadmin import views
from .models import *


class TeamAdmin(object):
	list_display = ['name', 'code']


class RoleAdmin(object):
	list_display = ['index', 'name']


class UserProfileAdmin(object):
	list_display = ['name', 'gender']
	search_fields = ['id', 'name', 'email', 'mobile']  # 要查询的列
	list_filter = ("gender",)
	readonly_fields = ("id",)


class VerifyCodeAdmin(object):
	list_display = ['code', 'mobile']


class BaseSetting(object):
	enable_themes = True
	use_bootswatch = True


xadmin.site.register(Team, TeamAdmin)
xadmin.site.register(Role, RoleAdmin)
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
