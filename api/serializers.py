from rest_framework import serializers
from .models import WebringModel

class WebringSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebringModel
        fields = ['id', 'name', 'status', 'last_updated', 'description', 'url']
