#!encoding:utf-8
from rest_framework import serializers
from community.models import *

class TechnologySerializers(serializers.ModelSerializer):
	class Meta:
		model = Technology
		fields = ("name",)

