# encoding: utf-8
from rest_framework import serializers

from directory_tree.models import DirectoryTree
from user_operation.models import Notes
from video.models import Video


class DirectoryTreeSerializers(serializers.ModelSerializer):
	class Meta:
		model = DirectoryTree
		fields = ("name",)


class VideoSerializers(serializers.ModelSerializer):
	video = DirectoryTreeSerializers()

	class Meta:
		model = Video
		fields = ("video",)


class NotesListSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)
	user = serializers.CharField(
		default=serializers.CurrentUserDefault()
	)
	video = VideoSerializers()
	updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H-%M")

	class Meta:
		model = Notes
		fields = (
			"_id", "user", "video", "title", "notes", "approve", "oppose", "is_show", "reprint_count", "updated_at")


class NotesSerializers(serializers.ModelSerializer):
	class Meta:
		model = Notes
		fields = ("title", "notes",)


class NotesCreateSerializers(serializers.ModelSerializer):
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)
	video = serializers.CharField(label="视频_id", min_length=24, max_length=24, required=True, write_only=True)
	title = serializers.CharField(label="标题", required=True, max_length=255)
	notes = serializers.CharField(label="笔记内容", required=True)

	def create(self, validated_data):
		note = super(NotesCreateSerializers, self).create(validated_data=validated_data)
		return note

	def validate_video(self, video):
		videos = Video.objects.filter(pk=video)
		if not videos.exists():
			raise serializers.ValidationError("视频不存在")
		video = videos[0]
		return video

	class Meta:
		model = Notes
		fields = ("title", "notes", "video", "user")
