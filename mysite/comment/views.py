from django.shortcuts import render
from rest_framework import viewsets

from comment.models import Comment
from  rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from comment.serializer import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




# Create your views here.
