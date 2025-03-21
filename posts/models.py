from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"

    POST_TYPES = [
        (TEXT, "Text"),
        (IMAGE, "Image"),
        (VIDEO, "Video"),
    ]

    title = models.CharField(max_length=255, default="Untitled Post")
    content = models.TextField(blank=True)
    post_type = models.CharField(max_length=10, choices=POST_TYPES, default=TEXT)
    metadata = models.JSONField(default=dict, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on Post {self.post.id}"
