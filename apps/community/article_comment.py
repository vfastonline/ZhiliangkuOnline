#!encoding:utf-8

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import authentication
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from community.article_comment_serializers import *


class ArticleCommentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
							viewsets.GenericViewSet):
	"""
	list:
		查看文章评论
	create:
		添加文章评论
	delete:
		删除文章评论
	"""

	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = ArticleComments.objects.all()

	filter_backends = (DjangoFilterBackend,)
	filter_fields = ("user_id", "article_id")

	def get_serializer_class(self):
		if self.action == "create":
			return ArticleCreateCommentsSerializers
		else:
			return ArticleCommentsSerializers


class SpecifyArticleCommentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取指定文章评论
	"""

	authentication_classes = ()
	permission_classes = ()
	serializer_class = ArticleCommentsSerializers
	queryset = ArticleComments.objects.all()
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ("article_id",)
