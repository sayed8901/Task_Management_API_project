from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Comment
from .serializers import CommentSerializer
from accounts.permissions import IsAdmin, IsMember, IsAdminOrReadOnly

# Create your views here.
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdmin | IsMember]
