#!encoding:utf-8
from __future__ import unicode_literals

from tracks_learning.models import Video
from users.models import *


class Faq(BaseModelMixin):
	REWARD = (
		("0", "不悬赏"),
		("2", "2积分"),
		("3", "3积分"),
		("4", "4积分"),
		("5", "5积分"),
	)

	STATUS = (
		("0", "未解决"),
		("1", "已解决"),
	)

	video = models.ForeignKey(Video, verbose_name="视频", limit_choices_to={'type__in': [1, 2]}, related_name="VideoFaq",
							  on_delete=models.CASCADE, blank=True)
	user = models.ForeignKey(UserProfile, verbose_name="提问用户", related_name="UserProfileFaq", on_delete=models.CASCADE)
	title = models.CharField(max_length=200, verbose_name='标题')
	description = models.TextField(verbose_name='问题描述')
	reward = models.CharField('悬赏', max_length=1, choices=REWARD, default="0")
	create_time = models.DateTimeField(verbose_name='提问时间', auto_now=True)
	browse_amount = models.PositiveIntegerField('浏览次数', default=0)
	status = models.CharField('状态', max_length=1, choices=STATUS, default="0")
	follow_user = models.ManyToManyField(UserProfile, verbose_name="关注用户", blank=True,
										 related_name="UserProfileAttentionFaq")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "问题"
		verbose_name_plural = verbose_name


class FaqAnswer(BaseModelMixin):
	faq = models.ForeignKey(Faq, verbose_name="问答题目", related_name="FaqAnswer", on_delete=models.CASCADE)
	user = models.ForeignKey(UserProfile, verbose_name="回答用户", related_name="UserProfileFaqAnswer",
							 on_delete=models.CASCADE)
	answer = models.TextField(verbose_name='回答')
	create_time = models.DateTimeField(verbose_name='回答时间', auto_now=True)
	approve = models.PositiveIntegerField('支持', default=0)
	oppose = models.PositiveIntegerField('反对', default=0)
	optimal = models.BooleanField("最佳答案", default=False, blank=True)

	def __str__(self):
		return self.faq.title

	class Meta:
		verbose_name = "问题-回答"
		verbose_name_plural = verbose_name


class FaqAnswerFeedback(BaseModelMixin):
	"""问题-回答 反馈"""
	faqanswer = models.ForeignKey(FaqAnswer, verbose_name="问题-回答", related_name="FaqAnswerFeedback",
								  on_delete=models.CASCADE)
	user = models.ForeignKey(UserProfile, verbose_name="反馈用户", related_name="UserProfileFaqAnswerFeedback",
							 on_delete=models.CASCADE)
	feedback = models.CharField(max_length=200, verbose_name='支持/反对')

	def __str__(self):
		return self.feedback

	class Meta:
		verbose_name = "问题-回答 反馈"
		verbose_name_plural = verbose_name


class FaqAnswerReply(BaseModelMixin):
	faqanswer = models.ForeignKey(FaqAnswer, verbose_name="问题回答", related_name="FaqAnswerReply",
								  on_delete=models.CASCADE)
	user = models.ForeignKey(UserProfile, verbose_name="回复用户", related_name="UserProfileFaqAnswerReply",
							 on_delete=models.CASCADE)
	reply = models.TextField(verbose_name='回复')
	create_time = models.DateTimeField(verbose_name='回复时间', auto_now=True)

	def __str__(self):
		return self.reply

	class Meta:
		verbose_name = "问题-回答-回复"
		verbose_name_plural = verbose_name
