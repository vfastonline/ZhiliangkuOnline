from django.db import models

from utils.model import BaseModelMixin


class DirectoryTree(BaseModelMixin):
	"""
	目录树
	"""
	CATEGORY_TYPE = (
		("direction", "方向"),
		("project", "项目"),
		("course", "课程"),
		("section", "章节"),
		("video", "视频"),
		("exercise", "练习"),
		("assessment", "考核"),
	)

	category = models.CharField(choices=CATEGORY_TYPE, verbose_name="类目", help_text="类目", max_length=30, default="")
	name = models.CharField(max_length=255, verbose_name="名称", help_text="名称")
	parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="父类目",
							   help_text="父目录",
							   related_name="sub_category")

	class Meta:
		verbose_name = "目录树"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name
