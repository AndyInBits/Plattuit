from django.db.models.signals import post_migrate
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import MyUserProfile

@receiver(post_migrate)
def create_default_user(sender, **kwargs):
    if sender.name == 'users':  
        if not MyUserProfile.objects.filter(user__username='andyvz91').exists():
            user = User.objects.create_user('andy_user', password='P@ssw0rd')
            user.save()
            
            user_profile = MyUserProfile(user=user)
            user_profile.save()