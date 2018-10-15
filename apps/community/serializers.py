#!encoding:utf-8
from rest_framework import serializers

from community.models import *


class TechnicalLabelSerializers(serializers.ModelSerializer):
	class Meta:
		model = TechnicalLabel
		fields = ("name",)
