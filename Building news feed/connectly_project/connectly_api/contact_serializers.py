from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone']

    def validate_name(self, value):
        """Custom validation for name field"""
        if not value.replace(" ", "").isalpha():  # Allows spaces in names
            raise serializers.ValidationError("Name must contain only letters.")
        return value
    