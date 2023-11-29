# blog/models.py
from django.db import models
import random
import sys
import time

CATEGORY_CHOICES = [
    ("tech", "Tech"),
    ("sports", "Sports"),
    ("entertainment", "Entertainment"),
    ("politics", "Politics"),
    ("fashion", "Fashion"),
    ("food", "Food"),
    ("travel", "Travel"),
    ("other", "Other"),
]

def random_image_filename(instance, filename):
    num = random.randint(1, sys.maxsize)
    return f"blog/{num}_{filename}"

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=time.time())
    image = models.ImageField(upload_to=random_image_filename, default="default_image.jpg")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.post.title}"