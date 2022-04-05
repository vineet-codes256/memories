from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Memory
from .serializers import MemorySerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class MemoryViewSet(viewsets.ModelViewSet):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class LatestMemoriesList(APIView):
    def get(self, request, format=None):
        memories = Memory.objects.all()[:5]
        serializer = MemorySerializer(memories, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MemorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
