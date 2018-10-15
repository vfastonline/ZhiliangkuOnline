#!encoding:utf-8
from directory_tree.models import DirectoryTree
from technical_label.models import TechnicalLabel
from utils.model import *
from utils.model import BaseModelMixin


class Project(BaseModelMixin):
	"""
	项目
	"""
	direction = models.ForeignKey(DirectoryTree, verbose_name="方向", on_delete=models.CASCADE,
								  limit_choices_to={'CATEGORY_TYPE': "direction"})
	project = models.ForeignKey(DirectoryTree, verbose_name='项目', related_name='projects', blank=True, null=True,
								on_delete=models.SET_NULL, limit_choices_to={'category_type': "project"})
	desc = models.TextField(max_length=1000, verbose_name='简介', )
	technical_labels = models.ArrayModelField(
		model_container=TechnicalLabel,
		verbose_name="技术标签",
	)
	image = models.ImageField(upload_to='project', verbose_name="项目封面", blank=True)
	price = models.CharField(max_length=16, verbose_name="价格", default="限免")
	study = models.PositiveIntegerField(verbose_name="学习人数", default=0)
	course = models.PositiveIntegerField(verbose_name="课程数", default=0)
	section = models.PositiveIntegerField(verbose_name="章节数", default=0)
	stars = models.PositiveIntegerField(verbose_name="项目评星", default=5)
	hot = models.BooleanField(verbose_name="热度推荐", default=False, help_text="是够首页显示为热度推荐")
	new = models.BooleanField(verbose_name="新品推荐", default=False, help_text="是够首页显示为新品推荐")

	objects = models.DjongoManager()

	def __str__(self):
		return self.project.name

	class Meta:
		verbose_name = "项目"
		verbose_name_plural = verbose_name


class CommonQuestion(models.Model):
	"""
	项目常见问题
	"""
	project = models.ForeignKey(Project, verbose_name="视频", on_delete=models.CASCADE)
	question = models.CharField(max_length=200, verbose_name='问题')
	answer = models.TextField(verbose_name='回答')

	def __str__(self):
		return self.question

	class Meta:
		verbose_name = "视频常见问题"
		verbose_name_plural = verbose_name
