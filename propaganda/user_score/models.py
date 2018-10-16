# encoding: utf-8
from django.contrib.auth import get_user_model
from djongo import models

from utils.model import BaseModelMixin

User = get_user_model()


class ScoreItem(BaseModelMixin):
	"""
	得分项
	"""
	RULE = (
		("1", "学生"),
		("2", "老师"),
	)
	name = models.CharField(verbose_name="评分项", max_length=255, blank=True)
	desc = models.TextField(verbose_name="评分项描述", blank=True)
	rule = models.CharField(verbose_name="角色", max_length=1, choices=RULE)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "得分项"
		verbose_name_plural = verbose_name


class ScoreRecord(BaseModelMixin):
	"""
	得分记录
	"""
	score_item = models.ForeignKey(ScoreItem, verbose_name="得分项", blank=True, on_delete=models.CASCADE)
	score = models.PositiveIntegerField(verbose_name="得分", default=2, blank=True, help_text="得分")

	class Meta:
		abstract = True


class UserScore(BaseModelMixin):
	"""
	用户得分
	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
	score_records = models.ArrayModelField(
		model_container=ScoreRecord,
		verbose_name="等分记录",
	)
	feedback = models.TextField(verbose_name="意见反馈", blank=True)

	objects = models.DjongoManager()

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = "用户得分"
		verbose_name_plural = verbose_name
