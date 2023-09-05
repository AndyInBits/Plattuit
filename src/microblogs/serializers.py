from rest_framework import serializers
from .models import MicroblogPost

class MicroblogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroblogPost
        fields = '__all__'

    def validate_content(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("The content of the microblogpost cannot exceed 200 characters.")
        return value