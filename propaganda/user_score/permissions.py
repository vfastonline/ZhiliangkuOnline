# encoding: utf-8

from rest_framework import permissions


class BrowseScoreReportPermission(permissions.BasePermission):
	"""
	浏览班主任评分统计接口权限
	"""

	def has_permission(self, request, view):
		return request.user.has_perm("users.browse_score_report")
