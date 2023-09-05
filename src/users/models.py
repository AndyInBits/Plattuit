from django.contrib.auth.models import Group, User
from django.db import models


class MyUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
    

