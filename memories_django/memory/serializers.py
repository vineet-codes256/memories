from itertools import product
from rest_framework import serializers

from .models import Memory

class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'species',
            'weight',
            'length',
            'latitude',
            'longitude',
            'description',
            'timestamp',
            'get_photo'
        )