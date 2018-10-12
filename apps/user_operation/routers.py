#!encoding:utf-8
from user_operation.follow import *
from user_operation.report import *
from user_operation.user_info import *
from user_operation.user_notes import *
from utils.tools import router

router.register(r'user_info', UserInfoViewSet, base_name="user_info")

router.register(r'notes', NotesViewSet, base_name="notes")
router.register(r'specify_notes', SpecifyNotesViewSet, base_name="specify_notes")

router.register(r'report', ReportViewSet, base_name="report")
router.register(r'follow-user', FollowUserViewSet, base_name="follow-user")
