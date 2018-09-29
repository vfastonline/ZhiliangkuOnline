#!encoding:utf-8
from utils.tools import router
from .user_center import UserCenterViewSet

# 个人中心-对外版
router.register(r'user_basic_info', UserCenterViewSet, base_name="user_basic_info")

# 个人中心-对内版
