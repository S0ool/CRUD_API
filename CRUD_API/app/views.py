from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


class CreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class UpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

