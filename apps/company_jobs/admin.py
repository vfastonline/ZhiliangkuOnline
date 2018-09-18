#!encoding:utf-8

from django.contrib import admin

from apps.company_jobs.models import Company_jobs


@admin.register(Company_jobs)
class Company_jobsAdmin(admin.ModelAdmin):
	list_display = (
		'name', 'jobname', 'salary', 'work_exp', 'education', 'skillwords')
