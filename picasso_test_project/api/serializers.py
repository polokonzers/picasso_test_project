from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    '''Serializer for file model'''
    class Meta:
        model = File
        fields = ('__all__')
