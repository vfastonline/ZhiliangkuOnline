#!encoding:utf-8
from django.contrib import admin

from apps.assessment.models import *


@admin.register(DockerType)
class DockerTypeAdmin(admin.ModelAdmin):
	list_display = ("name", 'image', "port")
	search_fields = ('name', "image")


@admin.register(ContainerPort)
class ContainerPortAdmin(admin.ModelAdmin):
	list_display = ("container_id", 'port')
	search_fields = ('container_id', "port")


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
	list_display = ("assessment", "docker")
	search_fields = ('assessment', "docker")
