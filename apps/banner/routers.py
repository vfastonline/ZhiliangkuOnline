#!encoding:utf-8
from utils.tools import router
from .views import BannerViewSet

router.register(r'banners', BannerViewSet, base_name="banners")
