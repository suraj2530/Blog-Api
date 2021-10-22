from rest_framework import generics
from api import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Category
from api.permissions import IsOwnerOrReadOnly
from rest_framework import permissions


class CategoryList(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = serializers.CategorySerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = serializers.CategorySerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class CommentList(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = serializers.CommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class Commentdetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = serializers.CommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = serializers.UserSerializer

class UserDetails(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = serializers.UserSerializer

class PostList(generics.ListAPIView): 
  queryset = Post.objects.all()
  serializer_class = serializers.PostSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner= self.request.User)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = serializers.PostSerializer
  permission_classes = [IsOwnerOrReadOnly,permissions.IsAuthenticatedOrReadOnly]