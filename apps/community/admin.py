#!encoding:utf-8
from django.contrib import admin

from .models import *


@admin.register(Article)
class FaqAdmin(admin.ModelAdmin):
	list_display = (
		"user", 'title', "content", "technology", "direction", "approve", "oppose", "browse_number", "comment",
		"release", "hot")


@admin.register(ArticleComments)
class FaqAnswerAdmin(admin.ModelAdmin):
	list_display = ("user", 'note', "comment")


@admin.register(Faq)
class FaqAnswerAdmin(admin.ModelAdmin):
	list_display = ("user", "video", 'problem', "technology", "browse_number", "comment_number", "answer_number", "hot")


@admin.register(FaqAnswer)
class FaqAnswerAdmin(admin.ModelAdmin):
	list_display = ("user", "faq", 'answer', "approve", "oppose", "is_optimal", "is_show")
