from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework import serializers
from rest_framework import status

from utils.drf_response_handler import JsonResponse
from .models import UserResume

User = get_user_model()


class UserResumeSerializer(serializers.ModelSerializer):
	"""
	用户简历'序列化
	"""
	_id = serializers.CharField(max_length=24)

	class Meta:
		model = UserResume
		fields = "__all__"


class UserResumeViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	"""
	用户，简历信息
	"""
	serializer_class = UserResumeSerializer
	queryset = UserResume.objects.all()
	authentication_classes = ()
	permission_classes = ()
	lookup_field = "user__id"

	# 常用过滤器之DjangoFilterBackend, SearchFilter, OrderingFilter
	# filter_backends = (DjangoFilterBackend, filters.OrderingFilter)

	# filter_fields = ('category',)
	# ordering = ('index',)

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(queryset, many=True)
		return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, desc="success")
