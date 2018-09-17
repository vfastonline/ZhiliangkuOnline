# encoding: utf-8

from rest_framework import serializers

from banner.models import *


class BannerSerializer(serializers.ModelSerializer):
	# _id = serializers.CharField(max_length=24)
	category = serializers.CharField(max_length=1, required=True)

	class Meta:
		model = Banner
		fields = ('category', "index", "image", "desc")
