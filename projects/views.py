from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectSerializer
from accounts.permissions import IsAdminOrReadOnly

# Create your views here.
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]
