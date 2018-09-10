from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import *

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
	list_display = ('_id', 'username', 'email', 'name', 'is_staff')
	filter_horizontal = ('groups', 'user_permissions', 'roles', 'teams',)
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		(_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
									   'groups', 'user_permissions')}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
		("自定义", {
			'fields':
				('name', "gender", "birthday",
				 'roles', 'institution', 'teams', "computer_major",
				 "graduate", "education", "signature", 'mobile',)
		}),
	)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ['name', 'code']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	list_display = ['index', 'name']


@admin.register(VerifyCode)
class VerifyCodeAdmin(admin.ModelAdmin):
	list_display = ['code', 'phone']
