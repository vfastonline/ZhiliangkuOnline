#!encoding:utf-8
from user_resumes.user_career import UserCareerViewSet
from user_resumes.user_resume import UserResumeViewSet
from utils.tools import router

router.register(r'user_resume', UserResumeViewSet, base_name="user_resume")  # 个人简历
router.register(r'user_career', UserCareerViewSet, base_name="user_career")  # 求职意向
