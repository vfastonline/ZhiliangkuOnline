#!encoding:utf-8
from utils.tools import router
from .project_views import ProjectViewSet

router.register(r'projects', ProjectViewSet, base_name="projects")
