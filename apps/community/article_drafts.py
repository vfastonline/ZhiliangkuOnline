#!encoding:utf-8

from community.article import ArticleViewSet
from community.models import Article


class ArticleDraftsViewSet(ArticleViewSet):
	"""
	list:
		获取用户草稿箱
	create:
		添加用户草稿箱
	update:
		更新用户草稿箱
	partial_update:
		更新用户草稿箱-部分更新
	delete:
		删除用户草稿箱
	"""

	def get_queryset(self):
		return Article.objects.filter(user__username=self.request.user, release=False)
