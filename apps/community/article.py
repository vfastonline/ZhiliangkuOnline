#!encoding:utf-8
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import authentication
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from community.article_serializers import *


class ArticleViewSet(viewsets.ModelViewSet):
	"""
	list:
		获取用户文章
	create:
		添加用户文章
	update:
		更新用户文章
	partial_update:
		更新用户文章-部分更新
	delete:
		删除用户文章
	"""

	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = Article.objects.filter(release=True)

	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('user_id',)

	def get_serializer_class(self):
		if self.action == "list":
			return ArticleListSerializers
		return ArticleCreateSerializers


class SpecifyArticleViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	"""
	read:
		查看指定用户文章
	"""
	authentication_classes = ()
	permission_classes = ()
	serializer_class = ArticleListSerializers
	queryset = Article.objects.all()
