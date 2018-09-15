# encoding: utf-8
from django.contrib.auth import get_user_model

from utils.model import *
from utils.storage import *

User = get_user_model()


class UserResume(BaseModelMixin):
	"""
	用户简历
	"""
	ICON = "user_icon/defaultUserIcon.png"

	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
	icon = models.ImageField('头像', upload_to="user_resume_icon", storage=ImageStorage(), max_length=256, default=ICON,
							 blank=True)
	name = models.CharField(max_length=30, verbose_name="姓名", blank=True)
	work_years = models.CharField(max_length=50, verbose_name="工作年限", blank=True)
	education = models.CharField(max_length=50, verbose_name="最高学历", blank=True)
	in_service_status = models.CharField(max_length=50, verbose_name="在职状态", blank=True)
	current_company = models.CharField(max_length=255, verbose_name="现任公司", blank=True)
	current_position = models.CharField(max_length=255, verbose_name="现任职务", blank=True)
	advantage = models.TextField(verbose_name="我的优势", blank=True)

	def __str__(self):
		return self.user.name

	class Meta:
		verbose_name = "个人简历"
		verbose_name_plural = verbose_name
		index_together = ["user"]


class CareerObjective(BaseModelMixin):
	"""
	求职意向
	"""
	user_resume = models.ForeignKey(UserResume, verbose_name="求职意向", on_delete=models.CASCADE, blank=True,
									related_name="CareerObjectives")
	position = models.CharField(max_length=255, verbose_name="职务", blank=True)
	way_of_work = models.CharField(max_length=255, verbose_name="工作方式", blank=True)
	city = models.CharField(max_length=255, verbose_name="城市", blank=True)
	salary = models.CharField(max_length=255, verbose_name="薪资", blank=True)
	industry = models.CharField(max_length=255, verbose_name="行业", blank=True)
	is_first = models.BooleanField(default=False, verbose_name="首要意向", help_text="是否首要求职意向")

	def __str__(self):
		return self.position

	class Meta:
		verbose_name = "求职意向"
		verbose_name_plural = verbose_name


class WorkExperience(BaseModelMixin):
	"""工作经历"""
	user_resume = models.ForeignKey(UserResume, verbose_name="工作经历", on_delete=models.CASCADE, blank=True,
									related_name="WorkExperiences")
	company = models.CharField("公司名称", max_length=255, blank=True)
	position = models.CharField("职位名称", max_length=255, blank=True)
	start_time = models.DateField("在职起始时间", max_length=255, blank=True)
	end_time = models.DateField("在职终止时间", max_length=255, blank=True)
	content = models.TextField("工作内容", blank=True)

	def __str__(self):
		return self.company

	class Meta:
		verbose_name = "工作经历"
		verbose_name_plural = verbose_name


class ProjectExperience(BaseModelMixin):
	"""项目经验"""
	user_resume = models.ForeignKey(UserResume, verbose_name="项目经验", on_delete=models.CASCADE, blank=True,
									related_name="ProjectExperiences")
	name = models.CharField("项目名称", max_length=255, blank=True)
	role = models.CharField("角色", max_length=255, blank=True)
	url = models.URLField("项目链接", max_length=255, blank=True)
	start_time = models.DateField("项目起始时间", max_length=255, blank=True)
	end_time = models.DateField("项目终止时间", max_length=255, blank=True)
	description = models.TextField("项目描述", blank=True)
	performance = models.TextField("项目业绩", blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "项目经验"
		verbose_name_plural = verbose_name


class EducationExperience(BaseModelMixin):
	"""教育经历"""
	user_resume = models.ForeignKey(UserResume, verbose_name="教育经历", on_delete=models.CASCADE, blank=True,
									related_name="EducationExperiences")
	school = models.CharField("学校名称", max_length=255, blank=True)
	discipline = models.CharField("所学专业", max_length=255, blank=True)
	education = models.CharField("学历", max_length=255, blank=True)
	start_time = models.DateField("起始时间", max_length=255, blank=True)
	end_time = models.DateField("终止时间", max_length=255, blank=True)
	experience = models.TextField("在校经历", blank=True)

	def __str__(self):
		return self.school

	class Meta:
		verbose_name = "教育经历"
		verbose_name_plural = verbose_name
