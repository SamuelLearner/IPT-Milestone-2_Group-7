from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # Display author as a string

    class Meta:
        model = Post
        fields = ['id', 'content', 'created_at', 'author']  # Make sure 'author' is included

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['author'] = request.user  # Assign the logged-in user as the author
        return super().create(validated_data)
