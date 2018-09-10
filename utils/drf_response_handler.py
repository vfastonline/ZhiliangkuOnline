# encoding: utf-8
import ujson

from django.utils import six
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
	"""异常'接口响应'结果集
	:param exc:
	:param context:
	:return: { "msg":"Not allowed.", "code":400, "data":null }
	"""
	# Call REST framework's default exception handler first,
	# to get the standard error response.
	response = exception_handler(exc, context)

	# Now add the HTTP status code to the response.
	if response is not None:
		response.data['code'] = response.status_code

	return response


class JsonResponse(Response):
	"""通用'响应'结果集
	An HttpResponse that allows its data to be rendered into
	arbitrary media types.
	"""

	def __init__(self, data=None, code=None, detail="success", status=None, template_name=None, headers=None,
				 exception=False, content_type=None):
		"""
		Alters the init arguments slightly.
		For example, drop 'template_name', and instead use 'data'.
		Setting 'renderer' and 'media_type' will typically be deferred,
		For example being set automatically by the `APIView`.
		"""
		super(Response, self).__init__(None, status=status)

		if isinstance(data, Serializer):
			msg = (
				'You passed a Serializer instance as data, but '
				'probably meant to pass serialized `.data` or '
				'`.error`. representation.'
			)
			raise AssertionError(msg)

		self.data = {
			"code": code,
			"detail": detail,
			"data": data
		}
		self.template_name = template_name
		self.exception = exception
		self.content_type = content_type

		if headers:
			for name, value in six.iteritems(headers):
				self[name] = value
