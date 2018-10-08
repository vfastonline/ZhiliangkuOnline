# encoding: utf-8

from django.contrib.auth import get_user_model

from directory_tree.models import DirectoryTree
from utils.model import *

User = get_user_model()


class StudentNotes(BaseModelMixin):
	"""学生笔记"""
	user = models.ForeignKey(User, verbose_name="学生", on_delete=models.CASCADE)
	video = models.ForeignKey(DirectoryTree, verbose_name="视频", limit_choices_to={'category': "video"},
							  on_delete=models.CASCADE)
	title = models.CharField(max_length=200, verbose_name='标题')
	notes = models.TextField(verbose_name='笔记内容')

	approve = models.PositiveIntegerField(verbose_name='支持', default=0)
	oppose = models.PositiveIntegerField(verbose_name='反对', default=0)
	collection = models.PositiveIntegerField(max_length=256, verbose_name="采集", default=0)
	is_report = models.BooleanField(verbose_name="是否举报", default=False)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "学生笔记"
		verbose_name_plural = verbose_name


class Article(BaseModelMixin):
	"用户文章"
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", help_text="用户")
	title = models.CharField(max_length=200, verbose_name='标题')
	skill_label = models.CharField(max_length=10, verbose_name="技能标签")
	column = models.CharField(max_length=10, verbose_name="栏目")
	content = models.TextField(verbose_name='文章内容')

	approve = models.PositiveIntegerField(verbose_name='支持', default=0)
	oppose = models.PositiveIntegerField(verbose_name='反对', default=0)
	browse_number = models.PositiveIntegerField(verbose_name='浏览数', default=0)
	comment = models.PositiveIntegerField(verbose_name='评论数', default=0)
	is_report = models.BooleanField(verbose_name="是否举报", default=False)
	is_share = models.BooleanField(verbose_name='是否分享', default=False)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "用户文章"
		verbose_name_plural = verbose_name


class Userfollow(BaseModelMixin):
	"""用户关注 """

	user = models.ManyToManyField(User, verbose_name="用户", related_name='UserProfile',
								  on_delete=models.CASCADE)
	user_follow = models.ForeignKey(User, verbose_name="被关注用户", related_name='ToUserProfile',
									on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

	class Meta:
		unique_together = ('user', 'user_follow',)
		verbose_name = "用户关注"
		verbose_name_plural = verbose_name


class UserProblem(BaseModelMixin):
	"""
	用户问题
	"""
	user = models.ForeignKey(User, verbose_name="提问用户", related_name="UserProblems", on_delete=models.CASCADE)
	title = models.CharField(max_length=200, verbose_name='问题标题')
	video = models.ForeignKey(DirectoryTree, verbose_name="视频", limit_choices_to={'category': "video"},
							  on_delete=models.CASCADE)
	skill_label = models.CharField(max_length=10, verbose_name="技能标签")

	browse_amount = models.PositiveIntegerField('浏览次数', default=0)
	comment = models.PositiveIntegerField(verbose_name='评论次数', default=0)
	is_share = models.BooleanField(verbose_name='是否分享', default=False)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "问题"
		verbose_name_plural = verbose_name
		ordering = ["-updated_at"]


class QuestionAnswer(BaseModelMixin):
	"""
	问题-回答
	"""
	problem = models.ForeignKey(UserProblem, verbose_name="问答题目", related_name="QuestionAnswers",
								on_delete=models.CASCADE)
	user = models.ForeignKey(User, verbose_name="回答用户", related_name="UserQuestionAnswer",
							 on_delete=models.CASCADE)
	answer_content = models.TextField(verbose_name='回答内容')

	approve = models.PositiveIntegerField(verbose_name='支持数', default=0)
	oppose = models.PositiveIntegerField(verbose_name='反对数', default=0)
	comment = models.PositiveIntegerField(verbose_name='评论数', default=0)
	is_adopt = models.BooleanField(verbose_name="是否采纳", default=False, )

	def __str__(self):
		return self.problem.title

	class Meta:
		verbose_name = "问题-回答"
		verbose_name_plural = verbose_name
		ordering = ["-updated_at"]


class WishList(BaseModelMixin):
	"""
	愿望清单
	"""
	user = models.ForeignKey(User, verbose_name="提问用户", related_name="UserProblems", on_delete=models.CASCADE)
	project = models.ForeignKey(DirectoryTree, verbose_name="项目", limit_choices_to={'category': "project"},
								on_delete=models.CASCADE)

	def __str__(self):
		return self.project.name

	class Meta:
		verbose_name = "愿望清单"
		verbose_name_plural = verbose_name
		ordering = ["-updated_at"]
