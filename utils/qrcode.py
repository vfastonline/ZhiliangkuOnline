# encoding: utf-8

import qrcode
from django.http import HttpResponse
from django.utils.six import BytesIO


def generate_qrcode(request, data):
	params_dict = request.GET
	params = list()
	for key, val in params_dict.items():
		params.append("=".join([key, val]))
	if params:
		data += "?" + "&".join(params)
	img = qrcode.make(data)

	buf = BytesIO()
	img.save(buf)
	image_stream = buf.getvalue()

	response = HttpResponse(image_stream, content_type="image/png")
	return response
