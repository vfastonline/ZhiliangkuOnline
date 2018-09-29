# encoding: utf8
from django.contrib.auth import get_user_model

from utils.model import *

User = get_user_model()


class QuestionnaireScore(BaseModelMixin):
	"""
	问卷调查，成绩
	"""
	CATEGORY = (
		("iq", "iq"),
		("eq", "eq"),
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
	category = models.CharField(verbose_name='类别', max_length=1, choices=CATEGORY, db_index=True, help_text="类别")
	value = models.IntegerField(verbose_name='分值', blank=True)

	class Meta:
		verbose_name = '问卷成绩'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.user.username


class EQ(BaseModelMixin):
	"""
	EQ测试题
	"""
	title = models.TextField('题目标题', max_length=50, blank=True)
	option = models.ListField()

	class Meta:
		verbose_name = '职场素质'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.title


class IQ(BaseModelMixin):
	"""
	IQ测试题
	"""
	title = models.TextField('题目标题', max_length=50, blank=True)
	image = models.ImageField(max_length=100, upload_to="iq_image", blank=True)
	option = models.ListField(blank=True)

	class Meta:
		verbose_name = '逻辑能力'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.title
