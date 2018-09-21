#!encoding:utf-8
from utils.tools import router
from .views import DirectoryTreeViewSet

router.register(r'directory-tree', DirectoryTreeViewSet, base_name="directory-tree")
