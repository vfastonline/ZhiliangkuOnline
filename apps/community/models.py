#!encoding:utf-8
from __future__ import unicode_literals

from django.contrib.auth import get_user_model

from user_operation.models import BaseReport
from users.models import *
from video.models import Video

User = get_user_model()


class Article(BaseModelMixin):
	"""
	文章
	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者", help_text="作者")
	title = models.CharField(max_length=255, verbose_name='标题')
	content = models.TextField(verbose_name='文章内容')

	approve = models.PositiveIntegerField(verbose_name='支持', default=0)
	oppose = models.PositiveIntegerField(verbose_name='反对', default=0)
	browse_number = models.PositiveIntegerField(verbose_name='浏览数', default=0)

	comment = models.PositiveIntegerField(verbose_name='评论数', default=0)
	is_show = models.BooleanField(verbose_name="是否显示", default=True, help_text="举报核实后隐藏")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "文章"
		verbose_name_plural = verbose_name


class ReportArticle(BaseReport):
	"""
	被举报的用户文章
	"""
	article = models.ForeignKey(Article, verbose_name="文章", on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = "被举报的用户文章"
		verbose_name_plural = verbose_name


class ArticleComments(BaseModelMixin):
	"""
	文章评论
	"""
	user = models.ForeignKey(User, verbose_name="评论者", on_delete=models.CASCADE)
	note = models.ForeignKey(Article, verbose_name="文章", on_delete=models.CASCADE, db_index=True)
	comment = models.TextField(verbose_name='评论内容', blank=True, help_text="评论内容")

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = "文章评论"
		verbose_name_plural = verbose_name


class Faq(BaseModelMixin):
	"""
	问题
	"""
	video = models.ForeignKey(Video, verbose_name="视频", related_name="faqs", on_delete=models.CASCADE, blank=True)
	user = models.ForeignKey(User, verbose_name="提问用户", related_name="UserFaq", on_delete=models.CASCADE)
	title = models.CharField(max_length=200, verbose_name='问题标题', blank=True)

	browse_number = models.PositiveIntegerField(verbose_name='浏览数', default=0)
	comment = models.PositiveIntegerField(verbose_name='评论数', default=0)

	reprint = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, verbose_name="转载自", help_text="问题源",
								related_name="sub_reprint")
	reprint_count = models.PositiveIntegerField(verbose_name="转载", default=0)

	is_show = models.BooleanField(verbose_name="是否显示", default=True, help_text="举报核实后隐藏")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "问题"
		verbose_name_plural = verbose_name


class FaqAnswer(BaseModelMixin):
	"""
	问题-回答
	"""
	faq = models.ForeignKey(Faq, verbose_name="问题", related_name="faq_answers", on_delete=models.CASCADE)
	user = models.ForeignKey(User, verbose_name="回答用户", related_name="faq_answer_user",
							 on_delete=models.CASCADE)
	answer = models.TextField(verbose_name='回答')
	is_optimal = models.BooleanField("最佳答案", default=False)

	def __str__(self):
		return self.faq.title

	class Meta:
		verbose_name = "问题-回答"
		verbose_name_plural = verbose_name


class ReportFaq(BaseReport):
	"""
	被举报的用户提问
	"""
	faq = models.ForeignKey(Faq, verbose_name="用户提问", on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = "被举报的用户提问"
		verbose_name_plural = verbose_name
