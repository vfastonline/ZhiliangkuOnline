#!encoding:utf-8
from banner.views import BannerViewSet
from utils.tools import router

router.register(r'banners', BannerViewSet, base_name="banners")
