# encoding: utf-8

from django_filters import rest_framework as filters

from .models import *


class UserScoreDateFilter(filters.FilterSet):
	"""
	用户评分记录时间过滤
	"""
	start_date = filters.DateFromToRangeFilter(field_name="created_at", label="开始时间")
	end_date = filters.DateFromToRangeFilter(field_name="created_at", label="结束时间")
	team = filters.CharFilter(field_name="owner__team", label="班级_id")

	class Meta:
		model = UserScore
		fields = ['start_date', 'end_date', 'team']
