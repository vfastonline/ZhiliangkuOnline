# encoding: utf-8
from rest_framework import viewsets, mixins, serializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from medal.models import *


class GetMedalSerializers(serializers.Serializer):
	medal = serializers.SerializerMethodField()

	def get_medal(self, obj):
		return obj.medal.name


class UserMedalSerializers(serializers.ModelSerializer):
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)
	medals = GetMedalSerializers(many=True)

	class Meta:
		model = UserMedal
		fields = ["user", "medals"]


class UserMedalViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	serializer_class = UserMedalSerializers

	def get_queryset(self):
		return UserMedal.objects.filter(user__username=self.request.user)
