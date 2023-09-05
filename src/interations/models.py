from django.db import models
from microblogs.models import MicroblogPost
from users.models import MyUserProfile

class Like(models.Model):
    user = models.ForeignKey(MyUserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(MicroblogPost, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Dislike(models.Model):
    user = models.ForeignKey(MyUserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(MicroblogPost, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class View(models.Model):
    user = models.ForeignKey(MyUserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(MicroblogPost, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)