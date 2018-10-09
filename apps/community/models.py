#!encoding:utf-8
from __future__ import unicode_literals

from django.contrib.auth import get_user_model

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
	release = models.BooleanField(verbose_name="是否发布", default=True, help_text="文章是否加入草稿箱")
	hot = models.BooleanField(verbose_name="热门文章", default=False, help_text="是够首页显示为热门")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "文章"
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
	user = models.ForeignKey(User, verbose_name="提问用户", related_name="faq_users", on_delete=models.CASCADE)
	problem = models.TextField(verbose_name='问题', blank=True)
	browse_number = models.PositiveIntegerField(verbose_name='浏览数', default=0)
	comment_number = models.PositiveIntegerField(verbose_name='评论数', default=0)
	answer_number = models.PositiveIntegerField(verbose_name="回答数", default=0)
	is_show = models.BooleanField(verbose_name="是否显示", default=True, help_text="举报核实后隐藏")
	hot = models.BooleanField(verbose_name="热门问题", default=False, help_text="是够首页显示为热门问题")

	def __str__(self):
		return self.problem

	class Meta:
		verbose_name = "问题"
		verbose_name_plural = verbose_name


class FaqAnswer(BaseModelMixin):
	"""
	问题-回答
	"""
	faq = models.ForeignKey(Faq, verbose_name="问题", related_name="faq_answers", on_delete=models.CASCADE)
	user = models.ForeignKey(User, verbose_name="回答用户", related_name="faq_answer_user", on_delete=models.CASCADE)
	answer = models.TextField(verbose_name='回答')
	approve = models.PositiveIntegerField(verbose_name='赞', default=0)
	oppose = models.PositiveIntegerField(verbose_name='踩', default=0)
	is_optimal = models.BooleanField("最佳答案", default=False)
	is_show = models.BooleanField(verbose_name="是否显示", default=True, help_text="举报核实后隐藏")

	def __str__(self):
		return self.faq.problem

	class Meta:
		verbose_name = "问题-回答"
		verbose_name_plural = verbose_name
