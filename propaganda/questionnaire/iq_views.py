# encoding: utf-8
import os

from rest_framework import authentication
from rest_framework import mixins
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import *
from .serializers import OptionSerializer


class IQQuestionnaireScoreSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)
	option_1 = serializers.CharField(max_length=255, write_only=True, help_text="1-10题选项")
	option_2 = serializers.CharField(max_length=255, write_only=True, help_text="11-20题选项")
	option_3 = serializers.CharField(max_length=255, write_only=True, help_text="21-30题选项")
	option_4 = serializers.CharField(max_length=255, write_only=True, help_text="31-40题选项")
	option_5 = serializers.CharField(max_length=255, write_only=True, help_text="41-50题选项")
	option_6 = serializers.CharField(max_length=255, write_only=True, help_text="51-60题选项")
	value = serializers.CharField(max_length=255, read_only=True)

	def create(self, validated_data):
		script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "IQ_reslutAPI.py")
		option_1 = validated_data["option_1"]
		option_2 = validated_data["option_2"]
		option_3 = validated_data["option_3"]
		option_4 = validated_data["option_4"]
		option_5 = validated_data["option_5"]
		option_6 = validated_data["option_6"]

		commond_str = "python2 {script} '{option_1}' '{option_2}' '{option_3}' '{option_4}' '{option_5}' '{option_6}'".format(
			script=script, option_1=option_1, option_2=option_2,
			option_3=option_3, option_4=option_4,
			option_5=option_5, option_6=option_6)
		print(commond_str)
		output = os.popen(commond_str, "r")
		output_str = output.read()
		output.close()
		del validated_data["option_1"]
		del validated_data["option_2"]
		del validated_data["option_3"]
		del validated_data["option_4"]
		del validated_data["option_5"]
		del validated_data["option_6"]
		questionnaire_score = super(IQQuestionnaireScoreSerializer, self).create(validated_data=validated_data)
		questionnaire_score.value = output_str
		questionnaire_score.save()
		return questionnaire_score

	class Meta:
		model = QuestionnaireScore
		fields = ("user", "category", "option_1", "option_2", "option_3", "option_4", "option_5", "option_6", "value")


class IQSerializer(serializers.ModelSerializer):
	option = OptionSerializer(many=True)

	class Meta:
		model = IQ
		fields = ("title", "image", "option")


class IQPagination(PageNumberPagination):
	page_size = 100


class IQViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取指IQ测试题

	create:
		录入成绩
	"""
	queryset = IQ.objects.all()
	serializer_class = IQSerializer
	pagination_class = IQPagination
	# throttle_classes = (UserRateThrottle, AnonRateThrottle)

	def get_authenticators(self):
		if self.request.method == "POST":
			return [JSONWebTokenAuthentication(), authentication.SessionAuthentication()]
		return []

	def get_permissions(self):
		if self.action == "create":
			return [IsAuthenticated()]
		return []

	def get_serializer_class(self):
		if self.action == "list":
			return IQSerializer
		if self.action == "create":
			return IQQuestionnaireScoreSerializer
		return IQSerializer
