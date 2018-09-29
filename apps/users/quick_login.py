# encoding: utf-8
import re
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from ZhiliangkuOnline.settings import REGEX_MOBILE
from .models import VerifyCode

User = get_user_model()


class UserQuickLoginSerializer(serializers.ModelSerializer):
	mobile = serializers.CharField(label="手机号", help_text="手机号", required=True, allow_blank=False)

	code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="验证码",
								 error_messages={
									 "blank": "请输入验证码",
									 "required": "请输入验证码",
									 "max_length": "验证码必须是4位数字",
									 "min_length": "验证码必须是4位数字"
								 },
								 help_text="验证码")

	def create(self, validated_data):
		user_obj = User.objects.filter(username=validated_data["username"])
		if user_obj.exists():
			return user_obj[0]
		user = super(UserQuickLoginSerializer, self).create(validated_data=validated_data)
		temporary_password = "#".join([validated_data["username"], "rewq"])
		user.set_password(temporary_password)
		user.save()
		return user

	def validate_code(self, code):
		verify_records = VerifyCode.objects.filter(phone=self.initial_data["mobile"]).order_by("-created_at")
		if verify_records:
			last_record = verify_records[0]

			# five_minutes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
			# if five_minutes_ago > last_record.created_at:
			# 	raise serializers.ValidationError("验证码过期")

			if last_record.code != code:
				raise serializers.ValidationError("验证码错误")
		else:
			raise serializers.ValidationError("验证码错误")

	@staticmethod
	def validate_mobile(mobile):
		if not re.match(REGEX_MOBILE, mobile):
			raise serializers.ValidationError("请输入正确手机号")
		return mobile

	def validate(self, attrs):
		attrs["username"] = attrs["mobile"]
		del attrs["code"]
		return attrs

	class Meta:
		model = User
		fields = ("mobile", "code")


class UserQuickLoginViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
	"""
	create:
		短信+验证码，快捷登录
	"""
	queryset = User.objects.all()
	serializer_class = UserQuickLoginSerializer
	authentication_classes = ()
	permission_classes = ()

	def perform_create(self, serializer):
		user = serializer.save()
		return user

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = self.perform_create(serializer)

		data = serializer.data
		payload = jwt_payload_handler(user)
		data["token"] = jwt_encode_handler(payload)
		data["name"] = user.name if user.name else user.username

		headers = self.get_success_headers(serializer.data)
		return Response(data, status=status.HTTP_201_CREATED, headers=headers)
