# encoding: utf-8

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from utils.tools import index_decorator
from .models import *

User = get_user_model()


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	list_display = ['index', 'name']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ['name', 'invitations_code']


@admin.register(VerifyCode)
class VerifyCodeAdmin(admin.ModelAdmin):
	list_display = ['code', 'phone']


@admin.register(User)
class UserProfileAdmin(UserAdmin):
	list_display = ('_id', 'username', 'name', 'is_staff')
	filter_horizontal = ('groups', 'user_permissions', 'role', 'team',)
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		(_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
									   'groups', 'user_permissions')}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
		("自定义", {
			'fields':
				('name', "gender", "birthday",
				 'role', 'team', 'institution', "computer_major",
				 "graduate", "education", "signature", 'mobile',)
		}),
	)


# 后台页面设置，写在settings.py'INSTALLED_APPS首个的admin.py中
admin.site.site_header = "智量酷-数据后台管理系统"
admin.site.site_title = "智量酷"
admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)
