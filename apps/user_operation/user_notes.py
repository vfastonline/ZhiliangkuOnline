# encoding: utf-8
from rest_framework import authentication
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_operation.user_notes_serializers import *


class UserNotesViewSet(viewsets.ModelViewSet, viewsets.GenericViewSet):
	"""
	list:
		获取用户笔记
	create:
		添加用户笔记
	delete:
		删除用户笔记
	update:
		更新用户笔记
	partial_update:
		更新用户笔记-部分更新

	"""
	authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Notes.objects.filter(user__username=self.request.user)

	def get_serializer_class(self):
		if self.action == "create":
			return NotesCreateSerializers
		elif self.action == "list":
			return NotesListSerializers
		else:
			return NotesSerializers
