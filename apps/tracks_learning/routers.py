#!encoding:utf-8

from tracks_learning.technology_info import TechnologyListInfo
from utils.tools import router


router.register(r'technology_list_info', TechnologyListInfo, base_name="user_resume")#技术分类
# router.register(r'projects_info')
