#!encoding:utf-8
from rest_framework import serializers

from community.models import *


class FaqSerializers(serializers.ModelSerializer):
	class Meta:
		model = Faq
		fields = ("problem",)


class FaqAnswerSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)
	user = serializers.CharField(
		default=serializers.CurrentUserDefault()
	)
	faq = FaqSerializers(read_only=True)

	class Meta:
		model = FaqAnswer
		fields = ("_id", "faq", "user", "answer", "approve", "oppose", "is_optimal")


class FaqAnswerCreateSerializers(serializers.ModelSerializer):
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)
	faq = serializers.CharField(label="问题_id", min_length=24, max_length=24, required=True)
	answer = serializers.CharField(label="回答", required=True)

	def validate_faq(self, faq):
		faq = Faq.objects.filter(_id=faq)
		if not faq.exists():
			raise serializers.ValidationError("问题不存在")
		faq = faq[0]
		return faq

	def create(self, validated_data):
		answer = super(FaqAnswerCreateSerializers, self).create(validated_data=validated_data)
		return answer

	class Meta:
		model = FaqAnswer
		fields = ("faq", "user", "answer")
