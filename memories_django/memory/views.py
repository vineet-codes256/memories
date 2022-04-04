from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Memory
from .serializers import MemorySerializer

class LatestMemoriesList(APIView):
    def get(self, request, format=None):
        memories = Memory.objects.all()[:5]
        serializer = MemorySerializer(memories, many=True)
        return Response(serializer.data)

