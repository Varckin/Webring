from rest_framework import serializers
from .models import WebringModel

class WebringSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebringModel
        fields = ['name', 'status', 'last_updated', 'description', 'url']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if self.context.get('request').method == 'GET':
            representation.pop('last_updated', None)

            return representation
