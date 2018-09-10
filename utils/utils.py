# encoding: utf-8
import json
import ujson

from bson import ObjectId

# 手机号码正则表达式
REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"


class JSONEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, ObjectId):
			return str(o)
		return json.JSONEncoder.default(self, o)


def monkey_patch_jsonencoder():
	json.JSONEncoder = JSONEncoder


def monkey_patch_json():
	json.__name__ = 'ujson'
	json.dumps = ujson.dumps
	json.loads = ujson.loads


monkey_patch_json()
