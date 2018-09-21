# encoding: utf-8


# @admin.register(Technology)
# class TechnologyAdmin(admin.ModelAdmin):
# 	list_display = ("name", "desc", "video")
#
#
# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
# 	list_display = ("name", "technology", "sequence", "is_lock", "home_show", "pathwel", "video")
#
#
# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
# 	list_display = ("project", 'name',  "desc", "sequence", "update_time")
#
#
# @admin.register(Section)
# class SectionAdmin(admin.ModelAdmin):
# 	list_display = ("project", 'course', 'title', 'sequence', "desc")
#
# 	def project(self, obj):
# 		name = ""
# 		try:
# 			if obj.course:
# 				name = obj.course.project.name
# 		except:
# 			traceback.print_exc()
# 			logging.getLogger().error(traceback.format_exc())
# 		finally:
# 			return name
#
# 	project.short_description = "项目"
#
#
# @admin.register(Video)
# class VideoAdmin(admin.ModelAdmin):
# 	list_display = ("project", "course", "section", 'name', "type", "duration", 'sequence',)
#
# 	def project(self, obj):
# 		name = ""
# 		try:
# 			if obj.section:
# 				name = obj.section.course.project.name
# 		except:
# 			traceback.print_exc()
# 			logging.getLogger().error(traceback.format_exc())
# 		finally:
# 			return name
#
# 	def course(self, obj):
# 		name = ""
# 		try:
# 			if obj.section:
# 				name = obj.section.course.name
# 		except:
# 			traceback.print_exc()
# 			logging.getLogger().error(traceback.format_exc())
# 		finally:
# 			return name
#
# 	project.short_description = "项目"
# 	course.short_description = "课程"
#
# 	fieldsets = [
#
# 		('视频/练习题', {
# 			'classes': ('suit-tab', 'suit-tab-video',),
# 			'fields': ['section', "type", 'name', 'subtitle', "sequence", "duration", "desc", "notes", "experiment"]}),
#
# 		('考核信息', {
# 			'classes': ('suit-tab', 'suit-tab-assessment',),
# 			'fields': ['topic', "shell", "docker", "assess_time"]}),
#
# 		('保利威视', {
# 			'classes': ('suit-tab', 'suit-tab-polyv',),
# 			'fields': ['vid', 'data']}),
# 	]
# 	suit_form_tabs = (('video', '视频/练习题'), ('assessment', '考核'), ('polyv', '保利威视'))
#
# 	def suit_row_attributes(self, obj, request):
# 		css_class = {
# 			"2": 'success',
# 			"3": 'info',
# 		}.get(obj.type)
# 		if css_class:
# 			return {'class': css_class}
#
#
# @admin.register(UnlockVideo)
# class UnlockVideoAdmin(admin.ModelAdmin):
# 	list_display = ("video", "custom_user", "is_pass", "times")
#
#
# @admin.register(Nodus)
# class NodusAdmin(admin.ModelAdmin):
# 	list_display = ("video", "title", 'notes', "moment")
#
#
# @admin.register(CommonQuestion)
# class CommonQuestionAdmin(admin.ModelAdmin):
# 	list_display = ("video", "question", 'answer')
#
#
# @admin.register(StudentNotes)
# class StudentNotesAdmin(admin.ModelAdmin):
# 	list_display = ("video", "custom_user", "title", 'notes', "create_time")
