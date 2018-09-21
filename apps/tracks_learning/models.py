# encoding: utf8

# from apps.assessment.models import *


# class Technology(BaseModelMixin):
# 	"""技术方向"""
# 	name = models.CharField('名称', max_length=50)
# 	desc = models.TextField('简介', default='', blank=True)
# 	video = models.ForeignKey("Video", verbose_name='总考核', related_name='Technology', blank=True,
# 							  limit_choices_to={'type': 3}, help_text=u"针对本技术方向下所有项目的总考核", on_delete=models.CASCADE)
#
# 	def __str__(self):
# 		return self.name
#
# 	class Meta:
# 		verbose_name = "技术方向"
# 		verbose_name_plural = verbose_name
#
#
# class Project(BaseModelMixin):
# 	"""项目说明书"""
# 	name = models.CharField('名称', max_length=50)
# 	desc = models.TextField('简介', max_length=1000, blank=True, default='')
# 	technology = models.ForeignKey(Technology, verbose_name="技术分类", blank=True,on_delete=models.CASCADE)
# 	sequence = models.PositiveIntegerField('顺序', default=1, validators=[MinValueValidator(1)], help_text="技术分类下显示顺序")
# 	is_lock = models.BooleanField("锁定", default=True)
# 	home_show = models.BooleanField("首页展示", default=False)
# 	pathwel = models.ImageField('介绍图片', upload_to='project/%Y%m%d', storage=ImageStorage(),blank=True)
# 	video = models.ForeignKey("Video", verbose_name='项目考核', related_name='Project', blank=True,
# 							  limit_choices_to={'type': 3}, help_text=u"针对本项目下所有课程的考核", on_delete=models.CASCADE)
#
# 	def __str__(self):
# 		return self.name
#
# 	class Meta:
# 		verbose_name = "项目"
# 		verbose_name_plural = verbose_name
#
#
# class Course(BaseModelMixin):
# 	"""课程"""
#
# 	project = models.ForeignKey(Project, verbose_name='归属项目', related_name='Courses', blank=True,
# 								on_delete=models.CASCADE)
# 	name = models.CharField('名称', max_length=50)
# 	user = models.ForeignKey(UserProfile, verbose_name='讲师', related_name='Course_custom_user', blank=True, on_delete=models.CASCADE)
# 	desc = models.TextField('描述', default="", blank=True, )
# 	sequence = models.PositiveIntegerField('顺序', default=1, validators=[MinValueValidator(1)], help_text="默认顺序为1")
# 	update_time = models.DateTimeField("更新时间", auto_now=True)
#
# 	def __str__(self):
# 		return self.name
#
# 	class Meta:
# 		verbose_name = "课程"
# 		verbose_name_plural = verbose_name
#
#
# class Section(BaseModelMixin):
# 	"""课程-章节"""
# 	course = models.ForeignKey(Course, verbose_name='所属课程', related_name='Section', on_delete=models.CASCADE)
# 	title = models.CharField('章节标题', max_length=100, default='')
# 	desc = models.TextField('章节描述', default='', blank=True)
# 	sequence = models.PositiveIntegerField('章节顺序', default=1, validators=[MinValueValidator(1)], help_text="默认顺序为1")
#
# 	def __str__(self):
# 		return self.title
#
# 	class Meta:
# 		verbose_name = "章节"
# 		verbose_name_plural = verbose_name
#
#
# class Video(BaseModelMixin):
# 	TYPE = (
# 		("1", "视频"),
# 		("2", "练习题"),
# 		("3", "考核"),
# 	)
# 	section = models.ForeignKey(Section, verbose_name='所属章节', related_name='Videos', blank=True,
# 								on_delete=models.CASCADE)
# 	type = models.CharField('类型', max_length=1, choices=TYPE)
# 	name = models.CharField('视频/习题名称', max_length=255)
# 	subtitle = models.FileField('字幕', upload_to='video/%y%m%d', blank=True, default=' ')
# 	sequence = models.PositiveIntegerField('显示顺序', default=1, validators=[MinValueValidator(1)], help_text="从1开始，默认：1")
# 	duration = models.PositiveIntegerField('总时长', default=0, blank=True, help_text="视频成功上传后，由后台补全；单位：秒")
# 	desc = models.TextField('描述', default='', blank=True)
# 	notes = models.TextField('讲师笔记', default='',  blank=True)
# 	experiment = models.TextField('课后实验', default='',blank=True)
# 	topic = models.TextField('考核题目', default='',blank=True)
# 	shell = models.FileField('判题shell', upload_to='shell', storage=ShellStorage(), blank=True)
# 	docker = models.ForeignKey(DockerType, verbose_name='Docker类型', blank=True, on_delete=models.CASCADE)
# 	assess_time = models.PositiveIntegerField('考核时长(分)', default=5, help_text="考核时长，默认5分钟；单位：分")
#
# 	# 保利威视信息
# 	vid = models.CharField("vid", max_length=255, blank=True, help_text="由保利威视回调接口补充")
# 	data = models.TextField("视频信息", blank=True,help_text="由保利威视回调接口补充")
#
# 	def __str__(self):
# 		return self.name
#
# 	class Meta:
# 		verbose_name = "视频/练习题/考核"
# 		verbose_name_plural = verbose_name
#
#
# class UnlockVideo(BaseModelMixin):
# 	"""学生通过考核记录"""
# 	video = models.ForeignKey(Video, verbose_name="考核", related_name='UnlockVideos', limit_choices_to={'type': "3"},
# 							  on_delete=models.CASCADE)
# 	custom_user = models.ForeignKey(UserProfile, verbose_name='学生', related_name='UnlockVideoCustomUser',
# 									limit_choices_to={'role': 0}, blank=True, on_delete=models.CASCADE)
# 	is_pass = models.BooleanField("通过考核", default=False)
# 	times = models.PositiveIntegerField("考核次数", default=0)
# 	update_time = models.DateTimeField("更新时间", auto_now=True)
#
# 	def __str__(self):
# 		return self.video.name
#
# 	class Meta:
# 		verbose_name = "通过考核学生"
# 		verbose_name_plural = verbose_name
#
#
# class Nodus(BaseModelMixin):
# 	"""视频难点"""
# 	video = models.ForeignKey(Video, verbose_name="视频", limit_choices_to={'type': 1}, on_delete=models.CASCADE)
# 	title = models.CharField(max_length=200, verbose_name="标题")
# 	notes = models.TextField(verbose_name='解析')
# 	moment = models.PositiveIntegerField(verbose_name='视频时刻', help_text="单位：秒")
#
# 	def __str__(self):
# 		return self.title
#
# 	class Meta:
# 		verbose_name = "视频难点解析"
# 		verbose_name_plural = verbose_name
#
#
# class CommonQuestion(BaseModelMixin):
# 	"""视频常见问题"""
# 	video = models.ForeignKey(Video, verbose_name="视频", limit_choices_to={'type': 1}, on_delete=models.CASCADE)
# 	question = models.CharField(max_length=200, verbose_name='问题')
# 	answer = models.TextField(verbose_name='回答')
#
# 	def __str__(self):
# 		return self.question
#
# 	class Meta:
# 		verbose_name = "视频常见问题"
# 		verbose_name_plural = verbose_name
#
#
# class StudentNotes(BaseModelMixin):
# 	"""学生笔记"""
# 	video = models.ForeignKey(Video, verbose_name="视频", limit_choices_to={'type': 1}, on_delete=models.CASCADE)
# 	custom_user = models.ForeignKey(UserProfile, verbose_name="学生", blank=True,
# 									on_delete=models.CASCADE)
# 	title = models.CharField(max_length=200, verbose_name='标题')
# 	notes = models.TextField(verbose_name='笔记内容')
# 	create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)
#
# 	def __str__(self):
# 		return self.title
#
# 	class Meta:
# 		verbose_name = "学生笔记"
# 		verbose_name_plural = verbose_name
