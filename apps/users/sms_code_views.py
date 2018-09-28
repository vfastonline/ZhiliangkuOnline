# encoding: utf-8
from random import choice

import re
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from ZhiliangkuOnline.settings import APPKEY, SECRET
from utils.sms import SendSms
from .models import VerifyCode

User = get_user_model()
from ZhiliangkuOnline.settings import REGEX_MOBILE
from datetime import datetime, timedelta


class SmsCodeSerializer(serializers.Serializer):
	"""
	验证码， 序列化
	"""
	phone = serializers.CharField(max_length=11, help_text="手机号")

	@staticmethod
	def validate_phone(phone):
		if not re.match(REGEX_MOBILE, phone):
			raise serializers.ValidationError("手机号码非法")

		if User.objects.filter(mobile=phone).count():
			raise serializers.ValidationError("用户已经存在")

		one_minute_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
		if VerifyCode.objects.filter(created_at__gt=one_minute_ago, phone=phone).count():
			raise serializers.ValidationError("距离上一次发送未超过60s")

		return phone

	class Meta:
		model = VerifyCode
		fields = ('phone',)


class SmsCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):
	"""
	create:
		发送短信验证码
	"""
	authentication_classes = ()
	permission_classes = ()
	serializer_class = SmsCodeSerializer

	@staticmethod
	def generate_code():
		"""
		生成四位数字的验证码字符串
		"""
		seeds = "1234567890"
		random_str = []
		for i in range(4):
			random_str.append(choice(seeds))

		return "".join(random_str)

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		phone = serializer.validated_data["phone"]
		code = self.generate_code()

		send_sms = SendSms(APPKEY, SECRET)
		send_sms_result = send_sms.send_sms(phone, {'code': code})

		detail = send_sms_result.get("detail")
		data = {"phone": phone, "detail": detail}
		if send_sms_result.get("code") == 204:
			VerifyCode.objects.create(code=code, phone=phone)
			return Response(data=data, status=status.HTTP_201_CREATED)
		else:
			return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
