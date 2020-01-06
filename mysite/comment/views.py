from django.shortcuts import render
from rest_framework import viewsets

from comment.models import Comment
from  rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from comment.serializer import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Create your views here.
