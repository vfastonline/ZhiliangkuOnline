# encoding: utf-8
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import six
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import exception_handler

from ZhiliangkuOnline.settings import REST_FRAMEWORK


def custom_exception_handler(exc, context):
	"""异常'接口响应'结果集
	:param exc:
	:param context:
	:return: { "msg":"Not allowed.", "code":400 }
	"""
	# Call REST framework's default exception handler first,
	# to get the standard error response.
	response = exception_handler(exc, context)

	# Now add the HTTP status code to the response.
	if response is not None:
		response.data['code'] = response.status_code
		response.data['desc'] = response.data['detail']
		del response.data['detail']  # 删除detail字段

	return response


class JsonResponse(Response):
	"""通用'接口响应'结果集
	An HttpResponse that allows its data to be rendered into
	arbitrary media types.
	"""

	def __init__(self, data=None, code=None, desc=None,
				 status=None,
				 template_name=None, headers=None,
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
			"desc": desc,
			"data": data
		}
		self.template_name = template_name
		self.exception = exception
		self.content_type = content_type

		if headers:
			for name, value in six.iteritems(headers):
				self[name] = value


def api_paging(objs, request, Serializer):
	"""
	objs : 实体对象
	request : 请求对象
	Serializer : 对应实体对象的序列化
	"""
	try:
		page_size = int(request.GET.get('page_size', REST_FRAMEWORK.get("PAGE_SIZE", 10)))  # 每页显示条目数
		page = int(request.GET.get('page', 1))  # 页码
	except (TypeError, ValueError):
		return JsonResponse(code=status.HTTP_400_BAD_REQUEST, desc='page and page_size must be integer!')

	paginator = Paginator(objs, page_size)  # paginator对象
	total_count = paginator.count  # 记录总数
	num_pages = paginator.num_pages  # 总页数
	page_range = list(paginator.page_range)  # 页码列表
	try:
		objs = paginator.page(page)
	except PageNotAnInteger:
		objs = paginator.page(1)
	except EmptyPage:
		objs = paginator.page(paginator.num_pages)

	serializer = Serializer(objs, many=True)  # 序列化操作

	return JsonResponse(data={
		'detail': serializer.data,
		"total_count": total_count,
		'num_pages': num_pages,
		"page_range": page_range,
		'page': page,
		"page_size": page_size
	}, code=status.HTTP_200_OK, desc='page success')  # 返回
