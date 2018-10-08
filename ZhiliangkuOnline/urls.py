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
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework_swagger.views import get_swagger_view

from ZhiliangkuOnline.settings import MEDIA_ROOT, STATIC_ROOT, DEBUG
from banner.routers import *
from directory_tree.routers import *
from project.routers import *
from questionnaire.routers import *
from user_resumes.routers import *
from users.routers import *

schema_view = get_swagger_view(title="智量酷docs")

urlpatterns = [
	path('admin/', admin.site.urls),

	# 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
	re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
	re_path('static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),

	# 富文本相关url
	path('ueditor/', include('DjangoUeditor.urls')),

	# router的path路径
	re_path(r'^', include(router.urls)),

	# jwt'用户'token认证
	path('login/', obtain_jwt_token),  # 登录
	path('api-token-refresh/', refresh_jwt_token),  # 刷新token
	path('api-token-verify/', verify_jwt_token),  # 校验token

	# 调试登录
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

	# 第三方登录
	path('', include('social_django.urls', namespace='social')),

	# api文档
	path(r'docs/', include_docs_urls(title='接口文档', public=False)),
	path(r"docss/", schema_view),

	# 调查问卷
	path('questionnaire/', TemplateView.as_view(template_name='questionnaire.html'), name='questionnaire'),

	# 首页
	path('index/', TemplateView.as_view(template_name='index.html'), name='index'),

]

# debug模式，开启django调试工具
if DEBUG:
	import debug_toolbar

	urlpatterns += [path(r'__debug__/', include(debug_toolbar.urls))]
