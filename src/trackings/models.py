from django.db import models
from microblogs.models import MicroblogPost

class PostView(models.Model):
    post = models.ForeignKey(MicroblogPost, on_delete=models.CASCADE)
    views_count = models.PositiveIntegerField(default=0)

class PostInteraction(models.Model):
    post = models.ForeignKey(MicroblogPost, on_delete=models.CASCADE)
    likes_count = models.PositiveIntegerField(default=0)
    dislikes_count = models.PositiveIntegerField(default=0)