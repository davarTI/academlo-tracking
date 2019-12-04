from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
