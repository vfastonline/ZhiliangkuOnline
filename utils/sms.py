# encoding: utf8
import json
import logging
import traceback

from utils.alidayu import AlibabaAliqinFcSmsNumSendRequest

"""
异常：
{
    "error_response":{
        "sub_msg":"非法参数",
        "code":50,
        "sub_code":"isv.invalid-parameter",
        "msg":"Remote service error"
    }
}
{'error_response': {'code': 41, 'msg': 'Invalid arguments:sms_param', 'request_id': 'zpd4dzwdt3tz'}}
{'error_response': {'code': 15, 'msg': 'Remote service error', 'sub_code': 'isv.TEMPLATE_MISSING_PARAMETERS', 'sub_msg': '模板变量缺少对应参数值', 'request_id': '5rwwctq5mo6o'}}


正确响应
{
    "alibaba_aliqin_fc_sms_num_send_response":{
        "result":{
        }
    }
}
{'alibaba_aliqin_fc_sms_num_send_response': {'result': {'err_code': '0', 'model': '488307336466770265^0', 'msg': 'OK', 'success': True}, 'request_id': 'roay4jmbmnoe'}}
"""


class SendSms(object):

	def __init__(self, appkey, secret):
		self.appkey = appkey
		self.secret = secret
		self.url = "https://eco.taobao.com/router/rest"
		self.sms_type = 'normal'
		self.sms_free_sign_name = "智量酷"
		self.sms_template_code = "SMS_62900005"
		self.system_generate_version = "taobao-sdk-python-20170420"

	def send_sms(self, phone, sms_param):
		"""
		:param phone:
		:param sms_param:
		:return:
		"""

		result = {
			"code": 500,
			"detail": "验证码发送失败",
		}

		req = AlibabaAliqinFcSmsNumSendRequest(self.appkey, self.secret, self.url, self.system_generate_version)
		req.extend = ""
		req.sms_type = self.sms_type
		req.sms_free_sign_name = self.sms_free_sign_name
		req.sms_template_code = self.sms_template_code
		req.rec_num = phone
		req.sms_param = json.dumps(sms_param)
		logging.getLogger().info(req.sms_param)
		try:
			resp = req.getResponse()
			if "alibaba_aliqin_fc_sms_num_send_response" in resp:
				result = {
					"code": 204,
					"detail": resp["alibaba_aliqin_fc_sms_num_send_response"]["result"]["msg"],
				}
				logging.getLogger().info(resp)
				logging.getLogger().info(u'短信发送成功, phone:%s, sms_free_sign_name:%s, sms_template_code:%s 状态%s' % (
					req.rec_num, req.sms_free_sign_name, req.sms_template_code,
					resp['alibaba_aliqin_fc_sms_num_send_response']))
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return result
