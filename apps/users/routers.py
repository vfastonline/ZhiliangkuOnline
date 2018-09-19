#!encoding:utf-8
from utils.tools import router
from .sms_code_views import SmsCodeViewSet
from .user_views import UserViewSet

router.register(r'users', UserViewSet, base_name="users")

# 发验证码，每个手机号当天上限10条
router.register(r'sms_code', SmsCodeViewSet, base_name="sms_code")
