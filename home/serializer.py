from rest_framework import serializers
from .models import image

class imageserializer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields="__all__"