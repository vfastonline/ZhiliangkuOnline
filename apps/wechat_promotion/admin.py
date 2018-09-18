from django.contrib import admin
from apps.wechat_promotion.models import *


@admin.register(WechatBrowse)
class WechatBrowseAdmin(admin.ModelAdmin):
	list_display = ( "name", "pinyin", "remark", "page_views", "thumbs_up", "share")



@admin.register(WechatBackground)
class WechatBackgroundAdmin(admin.ModelAdmin):
	list_display = ( "sequence", "image")


@admin.register(WechatRemark)
class WechatRemarkAdmin(admin.ModelAdmin):
	list_display = ("name", "remark", "english")


@admin.register(WechatMusic)
class WechatMusicAdmin(admin.ModelAdmin):
	list_display = ( "name", "address", "images", "types")

