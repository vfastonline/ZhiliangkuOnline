# encoding: utf-8
from rest_framework import serializers

from .models import QuestionnaireScore


class OptionSerializer(serializers.Serializer):
	titleno = serializers.CharField(max_length=100)
	option = serializers.CharField(max_length=100)
	value = serializers.CharField(max_length=100)


class QuestionnaireScoreSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)

	class Meta:
		model = QuestionnaireScore
		fields = ("user", "category", "value", "consultant_email")
