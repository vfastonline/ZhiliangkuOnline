#!encoding:utf-8
from user_operation.user_medal import UserMedalViewSet
from utils.tools import router
from .follow import *
from .report import *
from .user_notes import *

router.register(r'notes', NotesViewSet, base_name="notes")
router.register(r'specify_notes', SpecifyNotesViewSet, base_name="specify_notes")
router.register(r'report', ReportViewSet, base_name="report")
router.register(r'follow_user', FollowUserViewSet, base_name="follow_user")
router.register(r'user_medal', UserMedalViewSet, base_name="user_medal")
