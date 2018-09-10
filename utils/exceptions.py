# encoding: utf-8
from rest_framework.exceptions import APIException


class ServiceUnavailable(APIException):
	"""
	服务不能正常访问异常
	"""
	status_code = 503
	default_detail = 'Service temporarily unavailable, try again later.'
