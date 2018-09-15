#!encoding:utf-8
from users.sms_code_views import SmsCodeViewSet
from users.user_views import UserViewSet
from utils.tools import router

router.register(r'users', UserViewSet, base_name="users")
router.register(r'send_sms', SmsCodeViewSet, base_name="send_sms")
