#!encoding:utf-8
from rest_framework import serializers

from community.models import ArticleComments, Article


class ArticleSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = Article
		fields = ("_id", "title")


class ArticleCommentsSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)
	user = serializers.CharField(
		default=serializers.CurrentUserDefault()
	)
	article = ArticleSerializers()

	class Meta:
		model = ArticleComments
		fields = ("_id", "user", "article", "comment")


class ArticleCreateCommentsSerializers(serializers.ModelSerializer):
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)
	article = serializers.CharField(label="文章_id", min_length=24, max_length=24, required=True)
	comment = serializers.CharField(label="评论内容", required=True)

	def create(self, validated_data):
		comment = super(ArticleCreateCommentsSerializers, self).create(validated_data=validated_data)
		return comment

	def validate_article(self, article):
		article = Article.objects.filter(_id=article)
		if not article.exists():
			raise serializers.ValidationError("文章不存在")
		article = article[0]
		return article

	class Meta:
		model = ArticleComments
		fields = ("user", "article", "comment")
