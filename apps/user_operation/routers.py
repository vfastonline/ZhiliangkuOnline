#!encoding:utf-8
from user_operation.user_info import *
from user_operation.user_notes import *
from utils.tools import router

router.register(r'user_info', UserInfoViewSet, base_name="user_info")
router.register(r'user_notes', UserNotesViewSet, base_name="user_notes")
