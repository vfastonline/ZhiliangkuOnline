# encoding: utf-8

from rest_framework import serializers

from .models import QuestionnaireScore


class QuestionnaireScoreSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)

	class Meta:
		model = QuestionnaireScore
		fields = ("user", "category", "value")
