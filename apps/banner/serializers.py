# encoding: utf-8

from rest_framework import serializers

from .models import *


class BannerSerializer(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = Banner
		fields = "__all__"
