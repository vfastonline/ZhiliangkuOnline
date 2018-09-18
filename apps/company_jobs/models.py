#!coding:utf-8
from __future__ import unicode_literals

from users.models import *


class Company_jobs(BaseModelMixin):
	name = models.CharField('公司名称', max_length=100, blank=True, )
	logo = models.ImageField('公司logo', max_length=100, blank=True, )
	salary = models.CharField('薪资范围', max_length=100, blank=True, )
	work_exp = models.CharField('工作经验', max_length=10, blank=True,)
	work_address = models.CharField('工作地址', max_length=200, blank=True,)
	education = models.CharField('学历', max_length=20, blank=True, )
	stype = models.CharField('是否全职', max_length=10, blank=True, )
	skillwords = models.CharField('技能关键词', max_length=100, blank=True,)
	phase = models.CharField('融资阶段', max_length=10, blank=True,)
	scale = models.CharField('人数规模', max_length=20, blank=True,)
	homepage = models.CharField('主页', max_length=200, blank=True, )
	jobname = models.CharField('职业名称', max_length=20, blank=True,)

	class Meta:
		verbose_name = "公司招聘职位"
		verbose_name_plural = verbose_name
