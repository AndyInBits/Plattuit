from django.db import models
from users.models import MyUserProfile

class MicroblogPost(models.Model):
    user = models.ForeignKey(MyUserProfile, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(MyUserProfile, related_name='liked_posts', blank=True)
    dislikes = models.ManyToManyField(MyUserProfile, related_name='disliked_posts', blank=True)

    def __str__(self):
        return self.content