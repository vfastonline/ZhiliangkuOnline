#!encoding:utf-8
from __future__ import unicode_literals

from tracks_learning.models import Video
from users.models import UserProfile
from utils.model import *


class Question(BaseModelMixin):
	RIGHTANSWER = (
		("1", "A"),
		("2", "B"),
		("3", "C"),
		("4", "D"),
	)
	video = models.ForeignKey(Video, verbose_name='所属视频', related_name='Questions', limit_choices_to={"type": "2"},
							  on_delete=models.CASCADE)
	title = models.CharField('问题内容', max_length=255)
	right_answer = models.CharField('正确答案', max_length=1, choices=RIGHTANSWER)
	detail = models.TextField('习题详解', max_length=255, default="")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "习题"
		verbose_name_plural = "习题"
		ordering = ["video"]
		index_together = ["video"]


class Answer(BaseModelMixin):
	RIGHTANSWER = (
		("1", "A"),
		("2", "B"),
		("3", "C"),
		("4", "D"),
	)
	question = models.ForeignKey(Question, verbose_name='所属习题', related_name='Answers', on_delete=models.CASCADE)
	option = models.CharField('选项', max_length=1, choices=RIGHTANSWER)
	content = models.TextField('内容', max_length=255, default="")

	def __str__(self):
		return self.content

	class Meta:
		verbose_name = "答案"
		verbose_name_plural = verbose_name
		ordering = ["question"]
		unique_together = (("question", "option"),)


class UserExercise(BaseModelMixin):
	"""用户的练习记录"""
	user = models.ForeignKey(UserProfile, verbose_name='学生',on_delete=models.CASCADE)
	video = models.ForeignKey(Video, verbose_name='所属视频',  on_delete=models.CASCADE)
	times = models.PositiveIntegerField("练习次数", default=1)
	is_pass = models.BooleanField("是否通过", default=False)
	current_time = models.DateTimeField("考核时间", auto_now=True)

	def __str__(self):
		return self.user.name

	class Meta:
		verbose_name = "用户练习记录"
		verbose_name_plural = verbose_name
