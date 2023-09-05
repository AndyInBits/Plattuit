from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MyUserProfile

class MyUserProfileCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    bio = serializers.CharField()

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username already exists')
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

        my_user_profile = MyUserProfile(
            user=user,
            bio=validated_data['bio'],
        )
        my_user_profile.save()

        return my_user_profile
