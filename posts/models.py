from django.db import models
from django.contrib.auth.models import User


class PostModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=2000)
    category = models.CharField(max_length=80, default='business')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}'s comment, on {self.created_at}"

    class Meta:
        ordering = ['created_at']


class ReplyModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}'s reply, to {self.post}, on {self.created_at}"

    class Meta:
        ordering = ['created_at']