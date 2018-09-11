from rest_framework import mixins, viewsets
from rest_framework.mixins import CreateModelMixin

from user_operation.serializers import *


class UserResumeViewSet(CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
						viewsets.GenericViewSet):
	"""
	用户
	"""
	serializer_class = UserResumeRegSerializer
	queryset = UserResume.objects.all()
	authentication_classes = ()
	permission_classes = ()
