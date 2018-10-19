# encoding: utf-8

from django.conf.urls import url
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

User = get_user_model()

app_name = 'user_score'
urlpatterns = [
	url('^index$', TemplateView.as_view(template_name='score_index.html')),
	url('^set_team$', TemplateView.as_view(template_name='score_set_team.html')),
	url('^report$', TemplateView.as_view(template_name='score_report.html'), name='report'),
]
