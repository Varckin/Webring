from rest_framework import serializers
from .models import WebringModel

class WebringSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebringModel
        fields = ['name', 'status', 'description', 'url']
