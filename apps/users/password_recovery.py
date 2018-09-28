# encoding: utf-8


from rest_framework import viewsets, mixins

from .serializers import *


class PassWordRetrieveSerializer(serializers.Serializer):
	mobile = serializers.CharField(max_length=11, help_text="手机号", required=True, label="手机号")
	code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="验证码",
								 error_messages={
									 "blank": "请输入验证码",
									 "required": "请输入验证码",
									 "max_length": "验证码必须是4位数字",
									 "min_length": "验证码必须是4位数字"
								 },
								 help_text="验证码")
	password = serializers.CharField(
		style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
	)

	@staticmethod
	def validate_mobile(mobile):
		if not re.match(REGEX_MOBILE, mobile):
			raise serializers.ValidationError("手机号码非法")

		if not User.objects.filter(mobile=mobile).count():
			raise serializers.ValidationError("用户不存在")

		return mobile

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
		return code

	def update(self, instance, validated_data):
		instance.set_password(validated_data["password"])
		instance.save()
		return instance


class PassWordRetrieveViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
	"""
	update:
		手机号，找回密码
	"""
	queryset = User.objects.all()
	authentication_classes = ()
	permission_classes = ()
	serializer_class = PassWordRetrieveSerializer
	lookup_field = "mobile"
