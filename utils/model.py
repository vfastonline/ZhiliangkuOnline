# encoding: utf8
from djongo import models


class BaseModelMixin(models.Model):
	"""
	基础模型，去掉了默认自增字段id
	"""
	_id = models.ObjectIdField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True
