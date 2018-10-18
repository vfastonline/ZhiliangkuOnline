#!encoding:utf-8
from utils.tools import router
from .follow import *
from .report import *
from .user_notes import *
from .user_personal_info import *

router.register(r'user_personal_info', UserPersonalInfoViewSet, base_name="user_personal_info")
router.register(r'notes', NotesViewSet, base_name="notes")
router.register(r'specify_notes', SpecifyNotesViewSet, base_name="specify_notes")
router.register(r'report', ReportViewSet, base_name="report")
router.register(r'follow_user', FollowUserViewSet, base_name="follow_user")
