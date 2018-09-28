#!encoding:utf-8
from utils.tools import router
from .password_retrieve import PassWordRetrieveViewSet
from .sms_code_views import SmsCodeViewSet
from .user_exists import UserExistsViewSet
from .user_views import UserViewSet

router.register(r'users', UserViewSet, base_name="users")

# 发验证码，每个手机号当天上限10条
router.register(r'sms_code', SmsCodeViewSet, base_name="sms_code")
router.register(r'user_exists', UserExistsViewSet, base_name="user_exists")
router.register(r'password_retrieve', PassWordRetrieveViewSet, base_name="password_retrieve")
