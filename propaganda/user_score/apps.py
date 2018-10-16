from django.apps import AppConfig


class UserScoreConfig(AppConfig):
	name = 'user_score'
	verbose_name = "用户评分"

	def ready(self):
		pass
