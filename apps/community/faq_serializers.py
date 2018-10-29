#!encoding:utf-8

from rest_framework import serializers

from .models import *


class VideoSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)
	video = serializers.SerializerMethodField()

	def get_video(self, obj):
		return obj.video.name

	class Meta:
		model = Video
		fields = ("_id", "video",)


class TechnicalLabelSerializers(serializers.ModelSerializer):
	class Meta:
		model = TechnicalLabel
		fields = ("name",)


class FaqSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)
	user = serializers.CharField(
		default=serializers.CurrentUserDefault()
	)
	video = VideoSerializers()
	updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")
	technical_labels = serializers.SerializerMethodField()

	def get_technical_labels(self, obj):
		technical_label = [technical_label.technical_label for technical_label in obj.technical_labels]
		technical_label_json = TechnicalLabelSerializers(technical_label, many=True,
														 context={'request': self.context['request']}).data
		return technical_label_json

	class Meta:
		model = Faq
		fields = (
			"_id", "video", "user", "problem", "technical_labels", "browse_number", "comment_number", "answer_number",
			"hot", "updated_at")


class FaqCreateSerializers(serializers.Serializer):
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)
	problem = serializers.CharField(label="问题", required=True)
	# video = serializers.CharField(label="视频_id", write_only=True, required=True)
	video = serializers.PrimaryKeyRelatedField(label="视频", required=True, queryset=Video.objects.all(), write_only=True)

	technical = serializers.PrimaryKeyRelatedField(
		label="技术标签", required=True,
		queryset=TechnicalLabel.objects.all(),
		write_only=True, )

	def create(self, validated_data):
		user = validated_data["user"]
		video = validated_data["video"]
		problem = validated_data["problem"]
		technical = validated_data["technical"]

		param = {
			"user": user,
			"video": video,
			"problem": problem,
			"technical_labels": [FaqTechnicalLabels(technical_label=technical)]
		}
		faq_obj = Faq.objects.create(**param)
		return faq_obj
