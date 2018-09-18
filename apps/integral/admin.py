#!encoding:utf-8
from django.contrib import admin

from apps.integral.models import *


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
	list_display = ('name', "gtype", "style", 'integral', "stock", "residue_stock", 'detail', "imagess")
	search_fields = ('name',)
	list_filter = ('gtype',)

	def suit_row_attributes(self, obj, request):
		css_class = {
			0: 'error',
		}.get(obj.residue_stock)
		if css_class:
			return {'class': css_class}

	def imagess(self, obj):
		return '<img src="%s" height="24" width="24" />' % (obj.images.url)

	imagess.allow_tags = True
	imagess.short_description = "商品图片"


@admin.register(ExchangeRecords)
class ExchangeRecordsAdmin(admin.ModelAdmin):
	list_display = (
		'user', "goods", "ship",  "ship_time",)

