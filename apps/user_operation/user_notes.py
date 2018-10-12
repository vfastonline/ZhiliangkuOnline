# encoding: utf-8
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import authentication
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_operation.user_notes_serializers import *


class NotesViewSet(viewsets.ModelViewSet):
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
	queryset = Notes.objects.all()

	filter_backends = (DjangoFilterBackend,)
	filter_fields = ("user_id",)

	def get_serializer_class(self):
		if self.action == "create":
			return NotesCreateSerializers
		elif self.action == "list":
			return NotesListSerializers
		else:
			return NotesSerializers


class SpecifyNotesViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	"""
	read:
		查看用户笔记
	"""
	authentication_classes = ()
	permission_classes = ()
	queryset = Notes.objects.all()
	serializer_class = NotesListSerializers
