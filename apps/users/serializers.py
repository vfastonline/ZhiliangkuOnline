# encoding: utf-8
import re
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ZhiliangkuOnline.settings import REGEX_MOBILE
from .models import VerifyCode, Team

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
	"""
	用户详情
	"""

	class Meta:
		model = User
		fields = ("username", "gender", "birthday", "email", "mobile", "icon")


class UserUpdateSerializer(serializers.ModelSerializer):
	"""
	修改，用户
	"""

	mobile = serializers.CharField(label="手机号", help_text="手机号")

	def validate_mobile(self, mobile):
		if not re.match(REGEX_MOBILE, mobile):
			raise serializers.ValidationError("手机号码非法")

		# 手机是否注册
		if User.objects.filter(mobile=mobile).count():
			raise serializers.ValidationError("手机号已经存在")

		return mobile

	class Meta:
		model = User
		fields = (
			"name", "gender", "birthday", "institution", "computer_major", "graduate", "education", "signature",
			"mobile",)


class UserRegisterSerializer(serializers.ModelSerializer):
	"""
	注册，用户
	"""
	mobile = serializers.CharField(label="手机号", help_text="手机号", required=True, allow_blank=False,
								   validators=[UniqueValidator(queryset=User.objects.all(), message="手机号已经存在")])

	code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="验证码",
								 error_messages={
									 "blank": "请输入验证码",
									 "required": "请输入验证码",
									 "max_length": "验证码必须是4位数字",
									 "min_length": "验证码必须是4位数字"
								 },
								 help_text="验证码")

	invitations_code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="邀请码",
											 error_messages={
												 "blank": "请输入邀请码",
												 "required": "请输入邀请码",
												 "max_length": "邀请码格式错误",
												 "min_length": "邀请码格式错误"
											 },
											 help_text="邀请码")

	password = serializers.CharField(
		style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
	)

	def create(self, validated_data):
		team = validated_data["team"]
		del validated_data["team"]

		user = super(UserRegisterSerializer, self).create(validated_data=validated_data)
		user.set_password(validated_data["password"])
		user.team.add(team)
		user.save()

		return user

	def validate_invitations_code(self, invitations_code):
		team_records = Team.objects.filter(code=invitations_code)
		if team_records:
			team_record = team_records[0]

			one_hours_ago = datetime.now() - timedelta(hours=1, minutes=0, seconds=0)
			if one_hours_ago > team_record.created_at:
				raise serializers.ValidationError("邀请码过期，有效期1小时")
		else:
			raise serializers.ValidationError("邀请码错误")
		return team_record

	def validate_code(self, code):
		verify_records = VerifyCode.objects.filter(phone=self.initial_data["mobile"]).order_by("-created_at")
		if verify_records:
			last_record = verify_records[0]

			five_minutes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
			if five_minutes_ago > last_record.created_at:
				raise serializers.ValidationError("验证码过期")

			if last_record.code != code:
				raise serializers.ValidationError("验证码错误")
		else:
			raise serializers.ValidationError("验证码错误")

	def validate(self, attrs):
		attrs["username"] = attrs["mobile"]
		attrs["team"] = attrs["invitations_code"]
		del attrs["code"]
		del attrs["invitations_code"]
		return attrs

	class Meta:
		model = User
		fields = ("mobile", "invitations_code", "code", "password")
