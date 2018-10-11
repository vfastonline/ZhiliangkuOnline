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
	video = VideoSerializers()

	class Meta:
		model = Notes
		fields = ("_id", "video", "title", "notes", "approve", "oppose", "is_show", "reprint_count")


class NotesSerializers(serializers.ModelSerializer):
	class Meta:
		model = Notes
		fields = ("title", "notes",)


class NotesCreateSerializers(serializers.ModelSerializer):
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)
	video = serializers.CharField(min_length=24, max_length=24, required=True, write_only=True)
	title = serializers.CharField(required=True, max_length=255)
	notes = serializers.CharField(required=True)

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
