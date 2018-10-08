# encoding: utf-8
from django.contrib.auth import get_user_model

from assessments.models import Assessment
from course.models import Course
from exercise.models import Question
from project.models import Project
from utils.model import *
from video.models import Video

User = get_user_model()


class BaseReport(BaseModelMixin):
	"""
	举报基础信息
	"""
	user = models.ForeignKey(User, verbose_name="举报者", on_delete=models.CASCADE)
	reason = models.TextField(verbose_name='理由', blank=True, help_text="举报理由")

	class Meta:
		abstract = True


class Notes(BaseModelMixin):
	"""
	用户笔记
	"""
	user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
	video = models.ForeignKey(Video, verbose_name="视频", on_delete=models.CASCADE)
	title = models.CharField(max_length=200, verbose_name='标题')
	notes = models.TextField(verbose_name='笔记内容')

	reprint = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, verbose_name="转载自", help_text="笔记源",
								related_name="reprint")
	reprint_count = models.PositiveIntegerField(verbose_name="转载", default=0)
	approve = models.PositiveIntegerField(verbose_name='支持', default=0)
	oppose = models.PositiveIntegerField(verbose_name='反对', default=0)
	is_show = models.BooleanField(verbose_name="是否显示", default=True, help_text="举报核实后隐藏")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "学生笔记"
		verbose_name_plural = verbose_name


class ReportNotes(BaseReport):
	"""
	被举报的用户笔记
	"""
	note = models.ForeignKey(Notes, verbose_name="笔记", on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = "被举报的用户笔记"
		verbose_name_plural = verbose_name


class Follow(models.Model):
	"""
	被关注者
	"""
	user = models.ForeignKey(User, verbose_name="用户", related_name='user', on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

	class Meta:
		abstract = True


class FollowUser(BaseModelMixin):
	"""
	关注用户
	"""

	user = models.ForeignKey(User, verbose_name="用户", related_name='user', on_delete=models.CASCADE, db_index=True)
	follow = models.ArrayModelField(
		model_container=Follow,
	)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = "关注用户"
		verbose_name_plural = verbose_name


class WishList(BaseModelMixin):
	"""
	愿望清单
	"""
	user = models.ForeignKey(User, verbose_name="用户", related_name="user", on_delete=models.CASCADE)
	project = models.ForeignKey(Project, verbose_name="项目", on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username, self.project.project.name

	class Meta:
		verbose_name = "愿望清单"
		verbose_name_plural = verbose_name


class ParticipateProject(BaseModelMixin):
	"""
	用户参与项目
	"""
	user = models.ForeignKey(User, verbose_name="用户", related_name="user", on_delete=models.CASCADE)
	project = models.ForeignKey(Project, verbose_name="项目", on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username, self.project.project.name

	class Meta:
		verbose_name = "用户参与项目"
		verbose_name_plural = verbose_name


class PracticeRecord(BaseModelMixin):
	"""
	用户练习记录
	"""
	user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
	video = models.ForeignKey(Question, verbose_name='练习题', on_delete=models.CASCADE)
	times = models.PositiveIntegerField("练习次数", default=0)
	is_pass = models.BooleanField("是否通过", default=False)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = "用户练习记录"
		verbose_name_plural = verbose_name


class LearnCourse(BaseModelMixin):
	"""
	用户学习课程
	"""
	user = models.ForeignKey(User, verbose_name="用户", related_name="user", on_delete=models.CASCADE)
	course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username, self.course.course.name

	class Meta:
		verbose_name = "用户学习课程"
		verbose_name_plural = verbose_name


class VideoWatchRecord(BaseModelMixin):
	"""
	视频观看记录
	"""
	user = models.ForeignKey(User, verbose_name="用户", related_name="user", on_delete=models.CASCADE)
	video = models.ForeignKey(Video, verbose_name="视频", on_delete=models.CASCADE)
	moment = models.IntegerField('观看时刻', default=0, help_text="秒")
	duration = models.IntegerField('累计观看时长', default=0, help_text="累计观看时长，秒")
	complete = models.BooleanField("是否看完", default=False)

	def __str__(self):
		return self.user.username, self.video.video.name

	class Meta:
		verbose_name = "视频观看记录"
		verbose_name_plural = verbose_name


class FavVideo(BaseModelMixin):
	"""
	用户收藏视频
	"""

	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
	video = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name="视频", help_text="视频")

	def __str__(self):
		return self.user.username, self.video.video.name

	class Meta:
		verbose_name = '用户收藏视频'
		verbose_name_plural = verbose_name
		unique_together = ("user", "video")


class AssessmentRecord(BaseModelMixin):
	"""
	用户考核记录
	"""
	user = models.ForeignKey(User, verbose_name='用户', related_name='UnlockVideoCustomUser', blank=True,
							 on_delete=models.CASCADE, db_index=True)
	assessment = models.ForeignKey(Assessment, verbose_name="考核", related_name='assessments', on_delete=models.CASCADE)
	is_pass = models.BooleanField("是否通过", default=False, help_text="是否通过")
	times = models.PositiveIntegerField("考核次数", default=0)

	def __str__(self):
		return self.user.username, self.assessment.assessment.name

	class Meta:
		verbose_name = "用户考核记录"
		verbose_name_plural = verbose_name


class GoldGetWay(models.Model):
	name = models.CharField(max_length=255, verbose_name='途径名称')
	amount = models.PositiveIntegerField(verbose_name='金币数', default=0)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True


class GoldRecord(BaseModelMixin):
	"""
	用户获得金币记录
	"""
	user = models.ForeignKey(User, verbose_name='用户', related_name='gold_records', blank=True, on_delete=models.CASCADE,
							 db_index=True)
	get_way = models.ArrayModelField(
		model_container=GoldGetWay,
	)
	total = models.PositiveIntegerField(verbose_name='金币总数', default=0)

	def __str__(self):
		return self.user.username, str(self.total)

	class Meta:
		verbose_name = "用户获得金币记录"
		verbose_name_plural = verbose_name


class ProjectLearnRate(BaseModelMixin):
	"""
	用户学习项目评级
	"""
	RATE = (
		("1", "及格"),
		("2", "优秀"),
		("3", "学霸"),
	)
	user = models.ForeignKey(User, verbose_name='用户', related_name='project_appraisal', blank=True,
							 on_delete=models.CASCADE,
							 db_index=True)
	project = models.ForeignKey(Project, verbose_name="项目", on_delete=models.CASCADE)
	rate = models.CharField(max_length=1, verbose_name="评级", choices=RATE, help_text="系统对用户的项目学习情况评级")

	def __str__(self):
		return self.user.username, self.project.project.name

	class Meta:
		verbose_name = "项目评定"
		verbose_name_plural = verbose_name


class ProjectAppraisal(BaseModelMixin):
	"""
	用户对项目评定
	"""
	user = models.ForeignKey(User, verbose_name='用户', related_name='project_appraisal', blank=True,
							 on_delete=models.CASCADE,
							 db_index=True)
	project = models.ForeignKey(Project, verbose_name="项目", on_delete=models.CASCADE)
	star = models.PositiveIntegerField(verbose_name='星级', default=1)
	desc = models.TextField(verbose_name='评论', blank=True, help_text="评论内容")

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = "项目评定"
		verbose_name_plural = verbose_name
