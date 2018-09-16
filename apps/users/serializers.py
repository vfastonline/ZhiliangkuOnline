# encoding: utf-8
import re
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import VerifyCode, Role
from utils.tools import REGEX_MOBILE

User = get_user_model()


class SmsSerializer(serializers.Serializer):
	phone = serializers.CharField(max_length=11)

	def validate_phone(self, phone):
		"""
		验证手机号码(函数名称必须为validate_ + 字段名)
		"""
		# 验证手机号码是否合法
		if not re.match(REGEX_MOBILE, phone):
			raise serializers.ValidationError("手机号码非法")

		# 手机是否注册
		if User.objects.filter(mobile=phone).count():
			raise serializers.ValidationError("用户已经存在")

		# 验证码发送频率
		one_minute_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
		# 添加时间大于一分钟以前。也就是距离现在还不足一分钟
		if VerifyCode.objects.filter(created_at__gt=one_minute_ago, phone=phone).count():
			raise serializers.ValidationError("距离上一次发送未超过60s")

		return phone

	class Meta:
		model = VerifyCode
		fields = ('code', 'phone')


class UserDetailSerializer(serializers.ModelSerializer):
	"""
	用户详情序列化
	"""

	class Meta:
		model = User
		fields = ("username", "gender", "birthday", "email", "mobile")


class RoleSerializer(serializers.ModelSerializer):
	"""
	用户角色-序列化
	"""

	class Meta:
		model = Role
		fields = ("index", "name")


class UserUpdateSerializer(serializers.ModelSerializer):
	"""
	修改用户序列化
	"""

	class Meta:
		model = User
		fields = (
			"name", "gender", "birthday", "institution", "computer_major", "graduate", "education", "signature",
			"mobile",)


class UserRegSerializer(serializers.ModelSerializer):
	code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="验证码",
								 error_messages={
									 "blank": "请输入验证码",
									 "required": "请输入验证码",
									 "max_length": "验证码格式错误",
									 "min_length": "验证码格式错误"
								 },
								 help_text="验证码")

	mobile = serializers.CharField(label="手机号", help_text="手机号", required=True, allow_blank=False,
								   validators=[UniqueValidator(queryset=User.objects.all(), message="手机号已经存在")])
	password = serializers.CharField(
		style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
	)

	# 调用父类的create方法，该方法会返回当前model的实例化对象即user。
	# 前面是将父类原有的create进行执行，后面是加入自己的逻辑
	def create(self, validated_data):
		user = super(UserRegSerializer, self).create(validated_data=validated_data)
		user.set_password(validated_data["password"])
		user.roles.add(Role.objects.get(index=0))
		user.save()
		return user

	def validate_code(self, code):
		# get与filter的区别: get有两种异常，一个是有多个，一个是一个都没有。
		# try:
		#     verify_records = VerifyCode.objects.get(mobile=self.initial_data["username"], code=code)
		# except VerifyCode.DoesNotExist as e:
		#     pass
		# except VerifyCode.MultipleObjectsReturned as e:
		#     pass

		# 验证码在数据库中是否存在，用户从前端post过来的值都会放入initial_data里面，排序(最新一条)。
		verify_records = VerifyCode.objects.filter(phone=self.initial_data["username"]).order_by("-created_at")
		if verify_records:
			# 获取到最新一条
			last_record = verify_records[0]

			if last_record.code != code:
				raise serializers.ValidationError("验证码错误")

			# 有效期为五分钟。
			five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
			if five_mintes_ago > last_record.created_at:
				raise serializers.ValidationError("验证码过期")
		else:
			raise serializers.ValidationError("验证码错误")

	# 不加字段名的验证器作用于所有字段之上。attrs是字段 validate之后返回的总的dict
	def validate(self, attrs):
		attrs["username"] = attrs["mobile"]
		del attrs["code"]
		return attrs

	class Meta:
		model = User
		fields = ("mobile", "code", "password")
