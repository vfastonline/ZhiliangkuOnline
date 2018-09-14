#!encoding:utf-8
from user_resumes.user_resume import UserResumeViewSet
from user_resumes.user_resume_information import UserResumeInformation
from utils.tools import router

# 个人简历，查改
router.register(r'user_resume', UserResumeViewSet, base_name="user_resume")

# 求职意向、工作经历、项目经验、教育经历，增删改
router.register(r'user_resume_information', UserResumeInformation, base_name="User_resume_information")  #
