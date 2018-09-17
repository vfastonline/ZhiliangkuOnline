#!encoding:utf-8
from users.sms_code_views import SmsCodeViewSet
from users.user_views import UserViewSet
from utils.tools import router

router.register(r'users', UserViewSet, base_name="users")

# 发验证码，每个手机号当天上限10条
router.register(r'send_sms', SmsCodeViewSet, base_name="send_sms")
