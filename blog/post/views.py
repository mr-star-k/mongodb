from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework_mongoengine import viewsets
from .serializers import ToolSerializer
from .models import Tool

class ToolViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer