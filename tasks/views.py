from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer
from accounts.permissions import IsAdmin, IsMember, IsAdminOrReadOnly

# Create your views here.
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdmin | IsMember]
