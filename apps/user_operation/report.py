#!encoding:utf-8

from rest_framework import mixins, viewsets
from rest_framework import serializers, authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_operation.models import Report


class ReportSerializers(serializers.ModelSerializer):
	user = serializers.CharField(
		default=serializers.CurrentUserDefault()
	)
	types = serializers.SerializerMethodField()

	def get_types(self, obj):
		return obj.get_types_display()

	class Meta:
		model = Report
		fields = ("user", "reason", "source", "types")


class ReportCreateSerializers(serializers.ModelSerializer):
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)

	class Meta:
		model = Report
		fields = ("user", "source","types" ,"reason",)


class ReportViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取举报信息
	create:
		添加举报信息
	"""

	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		if self.action == "list":
			return ReportSerializers
		else:
			return ReportCreateSerializers

	def get_queryset(self):
		return Report.objects.filter(user__username=self.request.user)
