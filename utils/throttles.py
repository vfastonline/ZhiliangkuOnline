# encoding: utf-8

from rest_framework.throttling import SimpleRateThrottle


class SendSmsRateThrottle(SimpleRateThrottle):
	"""
	发验证码频率，1个手机1天最多10次
	"""

	scope = 'send_sms'  # 显示频率的Key,在配置文件里需要有个跟这个同名

	def get_cache_key(self, request, view):
		print(111)
		return self.get_ident(request)  # 获取请求IP
