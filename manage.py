#!/usr/bin/env python
import os
import sys

from utils.utils import monkey_patch_jsonencoder, monkey_patch_json

monkey_patch_jsonencoder()
monkey_patch_json()

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
