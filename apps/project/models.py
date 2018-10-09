#!encoding:utf-8

from directory_tree.models import DirectoryTree
from utils.model import *
from utils.model import BaseModelMixin


class Project(BaseModelMixin):
	"""
	项目
	"""
	project = models.ForeignKey(DirectoryTree, verbose_name='项目', related_name='projects', blank=True, null=True,
								on_delete=models.SET_NULL, limit_choices_to={'category_type': "project"})
	image = models.ImageField(upload_to='project', verbose_name="项目封面", blank=True)
	hot = models.BooleanField(verbose_name="热度推荐", default=False, help_text="是够首页显示为热度推荐")
	new = models.BooleanField(verbose_name="新品推荐", default=False, help_text="是够首页显示为新品推荐")

	def __str__(self):
		return self.project.name

	class Meta:
		verbose_name = "项目"
		verbose_name_plural = verbose_name
