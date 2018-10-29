#!encoding:utf-8

from community.serializers import *
from .models import *


class TechnicalLabelSerializers(serializers.ModelSerializer):
	class Meta:
		model = TechnicalLabel
		fields = ("name",)


class ArticleListSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)
	user = serializers.CharField(
		default=serializers.CurrentUserDefault()
	)
	direction = serializers.SerializerMethodField()
	technical_labels = serializers.SerializerMethodField()
	updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H-%M")

	def get_direction(self, obj):
		return obj.direction.name

	def get_technical_labels(self, obj):
		technical_labels_list = [technical_label.name for technical_label in obj.technical_labels]
		return technical_labels_list

	class Meta:
		model = Article
		fields = (
			"_id", "user", "title", "content", "technical_labels", "direction", "approve", "oppose", "browse_number",
			"comment",
			"is_show", "release", "hot", "updated_at")


class ArticleCreateSerializers(serializers.ModelSerializer):
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)

	direction = serializers.CharField(label="方向", )
	technical_labels = serializers.CharField(label="技术标签", )
	hot = serializers.BooleanField(label="是否为热门文章")

	def validate_technical_labels(self, technical_labels):
		technology = TechnicalLabel.objects.filter(_id=technical_labels)
		if not technology.exists():
			raise serializers.ValidationError("技术标签不存在")
		technology = technology[0]
		return technology

	def validate_direction(self, direction):
		direction = DirectoryTree.objects.filter(_id=direction)
		if not direction.exists():
			raise serializers.ValidationError("项目方向不存在")
		direction = direction[0]
		return direction

	def create(self, validated_data):
		user = validated_data["user"]
		title = validated_data["title"]
		content = validated_data["content"]
		technical_labels = validated_data["technical_labels"]
		direction = validated_data["direction"]
		release = validated_data["release"]
		hot = validated_data["hot"]
		article_param = {
			"user": user,
			"title": title,
			"content": content,
			"technical_labels": [technical_labels],
			"direction": direction,
			"release": release,
			"hot": hot,
		}
		article = Article.objects.create(**article_param)
		return article

	class Meta:
		model = Article
		fields = ("user", "title", "content", "technical_labels", "direction", "release", "hot")
