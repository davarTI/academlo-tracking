from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WorkspaceSerializer
from .models import Workspace


# Create your views here.

class WorkspaceViewSet(viewsets.ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
