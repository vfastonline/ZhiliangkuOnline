# encoding: utf-8
import json

from bson import ObjectId

# 手机号码'正则表达式
REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"


# 重写json解码，适应mongodb，ObjectId
class JSONEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, ObjectId):
			return str(o)
		return json.JSONEncoder.default(self, o)


# 猴子补丁，扩展json解码
def monkey_patch_jsonencoder():
	json.JSONEncoder = JSONEncoder
