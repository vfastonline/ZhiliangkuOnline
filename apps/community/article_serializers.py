#!encoding:utf-8

from community.serializers import *


class DirectoryTreeSerializers(serializers.ModelSerializer):
	class Meta:
		model = DirectoryTree
		fields = ("name",)


class ArticleListSerializers(serializers.ModelSerializer):
	_id = serializers.CharField(max_length=24)
	user = serializers.CharField(
		default=serializers.CurrentUserDefault()
	)
	technology = TechnologySerializers()
	direction = DirectoryTreeSerializers()
	updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H-%M")

	class Meta:
		model = Article
		fields = (
			"_id", "user", "title", "content", "technology", "direction", "approve", "oppose", "browse_number",
			"comment",
			"is_show", "release", "hot", "updated_at")


class ArticleCreateSerializers(serializers.ModelSerializer):
	user = serializers.HiddenField(
		default=serializers.CurrentUserDefault()
	)

	technology = serializers.CharField(label="技术标签", required=True)
	direction = serializers.CharField(label="方向", required=True)

	def validate_technology(self, technology):
		technology = Technology.objects.filter(_id=technology)
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
		article = super(ArticleCreateSerializers, self).create(validated_data=validated_data)
		return article

	class Meta:
		model = Article
		fields = ("user", "title", "content", "technology", "direction", "release",)
