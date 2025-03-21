from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

class Task(models.Model):
    title = models.CharField(blank=True,max_length=250)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title