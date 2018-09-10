# encoding: utf-8
from random import choice

from rest_framework import status
from rest_framework.response import Response
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from users.models import VerifyCode
from users.serializers import SmsSerializer
from utils.sms import SendSms
from ZhiliangkuOnline.settings import APPKEY, SECRET


class SmsCodeViewset(MongoModelViewSet):
	"""
	发送短信验证码
	"""
	serializer_class = SmsSerializer
	queryset = VerifyCode.objects.all()

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

		mobile = serializer.validated_data["mobile"]

		send_sms = SendSms(APPKEY, SECRET)

		code = self.generate_code()

		sms_status = send_sms.send_sms(mobile, {'code': code})

		if not sms_status:
			return Response({
				"mobile": "短信发送失败"
			}, status=status.HTTP_400_BAD_REQUEST)
		else:
			code_record = VerifyCode(code=code, mobile=mobile)
			code_record.save()
			return Response({
				"mobile": mobile
			}, status=status.HTTP_201_CREATED)
