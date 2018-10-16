#!encoding:utf-8
from django.conf.urls import url

from utils.polyv.api_callback import PolyvCallBack
from .poly_upload_video import GetPolyvParam

urlpatterns = [
	url('^get-param$', GetPolyvParam.as_view()),
	url('^callback$', PolyvCallBack.as_view()),
]
