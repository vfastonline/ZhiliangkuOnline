#!encoding:utf-8
from utils.tools import router
from .direction_views import DirectionViewSet

router.register(r'directions', DirectionViewSet, base_name="directions")
