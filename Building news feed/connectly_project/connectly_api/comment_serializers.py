from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'user', 'text']

    def validate_text(self, value):
        """Ensure comment text is at least 5 characters long"""
        if len(value) < 5:
            raise serializers.ValidationError("Comment must be at least 5 characters long.")
        return value
