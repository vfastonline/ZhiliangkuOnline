from django.contrib.auth.models import AbstractUser
from mongoengine import *

from utils.model import *
from utils.storage import *


class Role(BaseModelMixin):
	"""
	用户角色
	一个用户可能有多个角色
	0：学生
	1：老师
	2：HR
	3：其他
	"""
	index = models.IntegerField(verbose_name="唯一标志")
	name = models.CharField(max_length=30, verbose_name="角色名称")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "角色"
		verbose_name_plural = verbose_name


class Team(BaseModelMixin):
	"""
	班级
	"""

	name = models.CharField('名称', max_length=255)
	# technology = models.ForeignKey('tracks_learning.Technology', verbose_name="技术分类", on_delete=models.CASCADE, blank=True)
	code = models.CharField(max_length=5, verbose_name="邀请码")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "班级"
		verbose_name_plural = verbose_name


class UserProfile(AbstractUser):
	"""
	用户表，新增字段如下
	"""

	GENDER_CHOICES = (
		("male", u"男"),
		("female", u"女")
	)

	ICON = "user_icon/defaultUserIcon.png"

	_id = models.ObjectIdField()
	name = models.CharField(max_length=30, verbose_name="姓名", blank=True)
	gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name="性别", blank=True)
	birthday = models.DateField(verbose_name="出生年月", blank=True)
	roles = models.ManyToManyField(Role, verbose_name='角色')
	icon = models.ImageField('头像', upload_to="user_icon", storage=ImageStorage(), max_length=256, default=ICON,
							 blank=True)
	institution = models.CharField('所在院校', max_length=255, blank=True)
	teams = models.ManyToManyField(Team, verbose_name="所在班级")
	computer_major = models.BooleanField(default=True, verbose_name="计算机专业")
	graduate = models.BooleanField(default=False, verbose_name="毕业")
	education = models.CharField(max_length=255, verbose_name="学历", blank=True)
	signature = models.TextField(max_length=255, verbose_name='个性签名', blank=True)
	mobile = models.CharField(max_length=11, verbose_name="电话", help_text="联系电话", blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="最近一次更新")

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = "用户"
		verbose_name_plural = verbose_name


class VerifyCode(BaseModelMixin):
	"""
	短信验证码,回填验证码进行验证。可以保存在redis中
	"""
	code = models.CharField(max_length=10, verbose_name="验证码")
	phone = models.CharField(max_length=11, verbose_name="手机号")

	def __str__(self):
		return self.phone + ":" + self.code

	class Meta:
		verbose_name = "短信验证"
		verbose_name_plural = verbose_name
