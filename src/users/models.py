from django.contrib.auth.models import User, Group
from django.db import models

class MyUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_groups = models.ManyToManyField(Group)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.username
    

