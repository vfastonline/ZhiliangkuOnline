#!encoding:utf-8
from __future__ import unicode_literals

from django.apps import AppConfig


class CommunityConfig(AppConfig):
	name = 'community'
	verbose_name = "社区问答"
	main_menu_index = 10
