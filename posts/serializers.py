from rest_framework import serializers
from .models import User, Post, Comment

# USER SERIALIZER
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "created_at"]

# POST SERIALIZER
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "post_type", "metadata", "author", "created_at", "comments"]

# COMMENT SERIALIZER
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "text", "author", "post", "created_at"]

    def validate_author(self, value):
        """Ensure the author (user) exists in the database."""
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("Author not found.")
        return value

    def validate_post(self, value):
        """Ensure the post exists in the database."""
        if not Post.objects.filter(id=value).exists():
            raise serializers.ValidationError("Post not found.")
        return value

# CREATE POST SERIALIZER
class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["author", "post_type", "title", "content", "metadata"]

    def validate_post_type(self, value):
        valid_types = dict(Post.POST_TYPES).keys()
        if value not in valid_types:
            raise serializers.ValidationError(f"Invalid post type. Allowed types: {list(valid_types)}")
        return value
