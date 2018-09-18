# encoding: utf-8
from random import choice

from rest_framework import exceptions
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin

from ZhiliangkuOnline.settings import APPKEY, SECRET
from utils.drf_response_handler import *
from utils.sms import SendSms
from .models import VerifyCode
from .serializers import SmsSerializer


class SmsCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):
	"""
	发送短信验证码
	"""
	authentication_classes = ()
	permission_classes = ()
	serializer_class = SmsSerializer

	def generate_code(self):
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

		send_sms = SendSms(APPKEY, SECRET)
		code = self.generate_code()
		sms_status = send_sms.send_sms(phone, {'code': code})

		status = sms_status.get("code")
		desc = sms_status.get("detail")
		if sms_status.get("code") == 204:
			code_record = VerifyCode(code=code, phone=phone)
			code_record.save()

		return JsonResponse(desc=desc, code=sms_status.get("code"), status=status)

	def throttled(self, request, wait):
		"""
		访问次数被限制时，定制错误信息
		"""

		class Throttled(exceptions.Throttled):
			default_detail = '请求被限制.'
			extra_detail_singular = '请 {wait} 秒之后再重试.'
			extra_detail_plural = '请 {wait} 秒之后再重试.'

		raise Throttled(wait)
