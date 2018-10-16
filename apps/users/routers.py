#!encoding:utf-8
from utils.tools import router
from .get_team import GetTeamViewSet
from .password_retrieve import PassWordRetrieveViewSet
from .quick_login import UserQuickLoginViewSet
from .sms_code_views import SmsCodeViewSet
from .user_exists import UserExistsViewSet
from .user_info import UserInfoViewSet
from .user_views import UserViewSet

router.register(r'users', UserViewSet, base_name="users")
router.register(r'quick-login', UserQuickLoginViewSet, base_name="quick-login")
router.register(r'sms_code', SmsCodeViewSet, base_name="sms_code")
router.register(r'user_exists', UserExistsViewSet, base_name="user_exists")
router.register(r'password_retrieve', PassWordRetrieveViewSet, base_name="password_retrieve")
router.register(r'user_info', UserInfoViewSet, base_name="user_info")
router.register(r'get_team', GetTeamViewSet, base_name="get_team")
