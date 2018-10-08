#!encoding:utf-8


# @admin.register(Faq)
# class FaqAdmin(admin.ModelAdmin):
# 	list_display = (
# 		"video", 'title', "description", "reward", "user", "create_time", "browse_amount", "status")
#
#
# @admin.register(FaqAnswer)
# class FaqAnswerAdmin(admin.ModelAdmin):
# 	list_display = ("faq", "user", 'answer', "create_time", "approve", "oppose", "optimal")
#
#
# @admin.register(FaqAnswerReply)
# class FaqAnswerReplyAdmin(admin.ModelAdmin):
# 	list_display = ("faqanswer", 'reply', "user", "create_time")
#
#
# @admin.register(FaqAnswerFeedback)
# class FaqAnswerFeedbackAdmin(admin.ModelAdmin):
# 	list_display = ("faqanswer", 'user', "feedbacks")
#
#
# 	def feedbacks(self, obj):
# 		name = None
# 		try:
#
# 			if obj.feedback == "approve":
# 				name = True
# 			if obj.feedback == "oppose":
# 				name = False
# 		except:
# 			traceback.print_exc()
# 		finally:
# 			return name
#
# 	feedbacks.boolean = True
# 	feedbacks.short_description = "支持/反馈"
