#!encoding:utf-8
from utils.tools import router
from .consultant_views import ConsultantViewSet
from .eq_views import *
from .iq_views import *

router.register(r'eq', EQViewSet, base_name="eq")
router.register(r'iq', IQViewSet, base_name="iq")
router.register(r'consultant', ConsultantViewSet, base_name="consultant")
