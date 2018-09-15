#!encoding:utf-8

from django.core.validators import MinValueValidator

from utils.model import *
from utils.storage import *


class ProjectTechnology(BaseModelMixin):
	"""
	项目'技术方向
	"""
	name = models.CharField(max_length=50, verbose_name="名称", help_text="技术方向名称")
	desc = models.TextField(verbose_name='简介', blank=True)
	video = models.ForeignKey("Video", verbose_name='总考核', related_name='Technology', blank=True, null=True,
							  limit_choices_to={'type': 3}, help_text=u"针对本技术方向下所有项目的总考核", on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'Technology'
		verbose_name = "技术方向"
		verbose_name_plural = verbose_name


class Project(models.Model):
	"""项目说明书"""
	name = models.CharField('名称', max_length=50)
	desc = models.TextField('简介', max_length=1000, blank=True, null=True, default='')
	technology = models.ForeignKey(ProjectTechnology, verbose_name="技术分类", blank=True, null=True,
								   on_delete=models.CASCADE)
	sequence = models.PositiveIntegerField('顺序', default=1, validators=[MinValueValidator(1)], help_text="技术分类下显示顺序")
	is_lock = models.BooleanField("锁定", default=True)
	home_show = models.BooleanField("首页展示", default=False)
	pathwel = models.ImageField('介绍图片', upload_to='project/%Y%m%d', storage=ImageStorage(), null=True, blank=True)
	video = models.ForeignKey("Video", verbose_name='项目考核', related_name='Project', blank=True, null=True,
							  limit_choices_to={'type': 3}, help_text=u"针对本项目下所有课程的考核", on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'Project'
		verbose_name = "项目"
		verbose_name_plural = "项目"
		ordering = ['technology', "sequence"]
