#!encoding:utf-8

from directory_tree.models import DirectoryTree
from utils.model import *
from utils.model import BaseModelMixin


class Project(BaseModelMixin):
	"""
	项目
	"""
	project = models.ForeignKey(DirectoryTree, verbose_name='项目', related_name='project', blank=True, null=True,
								on_delete=models.SET_NULL, limit_choices_to={'category_type': "project"})
	is_home = models.BooleanField("首页展示", default=False)

	def __str__(self):
		return self.project.name

	class Meta:
		db_table = 'Project'
		verbose_name = "项目"
		verbose_name_plural = "项目"
