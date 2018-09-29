from directory_tree.models import DirectoryTree
from utils.model import *
from utils.model import BaseModelMixin


class Section(BaseModelMixin):
	"""
	章节
	"""
	section = models.ForeignKey(DirectoryTree, verbose_name='课程', related_name='sections', blank=True, null=True,
								on_delete=models.SET_NULL, limit_choices_to={'category_type': "course"})

	def __str__(self):
		return self.section.name

	class Meta:
		db_table = 'Section'
		verbose_name = "章节"
		verbose_name_plural = verbose_name


class Course(BaseModelMixin):
	"""
	课程
	"""
	course = models.ForeignKey(DirectoryTree, verbose_name='课程', related_name='courses', blank=True, null=True,
							   on_delete=models.SET_NULL, limit_choices_to={'category_type': "course"})

	def __str__(self):
		return self.course.name

	class Meta:
		db_table = 'Project'
		verbose_name = "项目"
		verbose_name_plural = verbose_name
