# encoding: utf-8
from django.contrib.auth import get_user_model
from rest_framework import authentication, serializers
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import *

User = get_user_model()


class TeamUserSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["name", "username"]


class TeamSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)
	teachers = serializers.SerializerMethodField()

	def get_teachers(self, team_obj):
		users = team_obj.team_users.all().filter(role__index=1)
		user_json = TeamUserSerializers(users, many=True, context={'request': self.context['request']}).data
		return user_json

	class Meta:
		model = Team
		fields = ["_id", "name", "teachers"]


class GetTeamViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	"""
	list:
		获取班级信息
	"""
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	queryset = Team.objects.all()
	serializer_class = TeamSerializers
