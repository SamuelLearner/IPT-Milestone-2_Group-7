from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User  # Import User model
from django.utils.timezone import now

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator()])
    phone = models.CharField(max_length=10, validators=[MinLengthValidator(10)], default="0000000000")

    def clean(self):
        """Custom validation logic"""
        if not self.name.replace(" ", "").isalpha():  # Allows spaces in names
            raise ValidationError({'name': 'Name must contain only letters.'})

    def __str__(self):
        return self.name

# Post Model
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Removed default=1
    content = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.author.username} - {self.created_at}"

# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f'Comment by {self.user.username} on "{self.post.content[:30]}..."'


