#!encoding:utf-8
from .views import BannerViewSet
from utils.tools import router

router.register(r'banners', BannerViewSet, base_name="banners")
