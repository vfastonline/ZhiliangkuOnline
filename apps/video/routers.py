#!encoding:utf-8
from utils.tools import router

router.register(r'user_resume', UserResumeViewSet, base_name="user_resume")
