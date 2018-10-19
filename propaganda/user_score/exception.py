# encoding: utf-8
from rest_framework.exceptions import APIException


class NoneTeamUnavailable(APIException):
	"""
	用户不归属任何班级
	"""
	status_code = 503
	default_detail = '用户不归属任何班级.'
