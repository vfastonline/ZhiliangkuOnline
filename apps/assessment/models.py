#!encoding:utf-8
from __future__ import unicode_literals

from directory_tree.models import DirectoryTree
from utils.model import *


class DockerType(BaseModelMixin):
	"""Docker 类型"""

	name = models.CharField('类型名称', max_length=255)
	image = models.CharField('镜像名称', max_length=255, help_text=u"固定并准确,用于创建docker时补全命令")
	port = models.CharField('镜像端口', max_length=10, help_text=u"先确认阿里云服务器开放端口并没有被其他镜像占用")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Docker类型"
		verbose_name_plural = verbose_name


class ContainerPort(BaseModelMixin):
	"""
	容器端口
	"""

	container_id = models.CharField('容器ID', max_length=255)
	port = models.CharField('端口', max_length=7)

	def __str__(self):
		return self.container_id, self.port

	class Meta:
		verbose_name = "容器端口"
		verbose_name_plural = verbose_name


class Assessment(BaseModelMixin):
	"""
	考核
	"""
	assessment = models.ForeignKey(DirectoryTree, verbose_name='考核', related_name='assessment', blank=True, null=True,
								   on_delete=models.SET_NULL, limit_choices_to={'category_type': "assessment"})
	topic = models.TextField('考核题目', default='', null=True, blank=True)
	docker = models.ForeignKey(DockerType, verbose_name='Docker类型', null=True, blank=True, on_delete=models.CASCADE)
	assess_time = models.PositiveIntegerField('考核时长(分)', default=5, help_text="考核时长，默认5分钟；单位：分")

	def __str__(self):
		return self.assessment.name

	class Meta:
		verbose_name = "考核"
		verbose_name_plural = verbose_name
