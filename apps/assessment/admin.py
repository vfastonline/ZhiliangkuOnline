#!encoding:utf-8
from django.contrib import admin

from apps.assessment.models import *
# from zhiliangku.settings import tinymce_js


@admin.register(DockerType)
class DockerTypeAdmin(admin.ModelAdmin):
	list_display = ( "name", 'image', "port", "introduce")
	search_fields = ('name', "image")

	# class Media:
	# 	js = tinymce_js


@admin.register(DockerPort)
class DockerPortAdmin(admin.ModelAdmin):
	list_display = ( "container", 'port', 'create', "maturity")
	search_fields = ('container', "port")
