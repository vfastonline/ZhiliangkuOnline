"""ZhiliangkuOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from django.contrib import admin
from ZhiliangkuOnline.settings import MEDIA_ROOT
from users.user_views import *
from users.sms_code_views import *

router = DefaultRouter()

# 配置codes的url
router.register(r'code', SmsCodeViewset, base_name="code")

# 配置users的url
router.register(r'users', UserViewset, base_name="users")

urlpatterns = [
	path('admin/', admin.site.urls),
	# path('xadmin/', xadmin.site.urls),

	# 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
	re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

	# 富文本相关url
	path('ueditor/', include('DjangoUeditor.urls')),

	# router的path路径
	re_path(r'^', include(router.urls)),

	# jwt的token认证
	path('login/', obtain_jwt_token),  # 登录
	path('api-token-refresh/', refresh_jwt_token),  # 刷新token
	path('api-token-verify/', verify_jwt_token),  # 校验token

]
