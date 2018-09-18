# encoding: utf-8

from rest_framework import serializers

from .models import *


class BannerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Banner
		fields = ("index", "image", "desc")
