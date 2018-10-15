#!encoding:utf-8

from rest_framework import serializers

from user_operation.user_notes_serializers import VideoSerializers
from .models import *


class FaqSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)
	user = serializers.CharField(
		default=serializers.CurrentUserDefault()
	)
	video = VideoSerializers()
	updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")

	class Meta:
		model = Faq
		fields = (
			"_id", "video", "user", "problem", "browse_number", "comment_number", "answer_number",
			"hot", "updated_at")


class FaqCreateSerializers(serializers.ModelSerializer):
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)
	video = serializers.CharField(label="视频_id", min_length=24, max_length=24, required=True, write_only=True)

	# technology = serializers.CharField(label="技术标签", min_length=24, max_length=24, required=True)

	def validate_video(self, video):
		videos = Video.objects.filter(_id=video)
		if not videos.exists():
			raise serializers.ValidationError("视频不存在")
		video = videos[0]
		return video

	# def validate_technology(self, technology):
	# 	technology = TechnicalLabel.objects.filter(_id=technology)
	# 	if not technology.exists():
	# 		raise serializers.ValidationError("技术标签不存在")
	# 	technology = technology[0]
	# 	return technology

	def create(self, validated_data):
		faq = super(FaqCreateSerializers, self).create(validated_data=validated_data)
		return faq

	class Meta:
		model = Faq
		fields = ("video", "user", "problem")
