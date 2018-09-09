#!/usr/bin/env python
import os
import sys

import json
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, ObjectId):
			return str(o)
		return json.JSONEncoder.default(self, o)


def monkey_patch_jsonencoder():
	json.JSONEncoder = JSONEncoder


monkey_patch_jsonencoder()

if __name__ == '__main__':
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZhiliangkuOnline.settings')
	try:
		from django.core.management import execute_from_command_line
	except ImportError as exc:
		raise ImportError(
			"Couldn't import Django. Are you sure it's installed and "
			"available on your PYTHONPATH environment variable? Did you "
			"forget to activate a virtual environment?"
		) from exc
	execute_from_command_line(sys.argv)
