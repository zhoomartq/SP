# from django.db.migrations import serializer
from django.shortcuts import render

from django.db import connection
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from project_api import serializers
from django.contrib.auth.models import User
from project_api.models import Post, Like, DisLike
from project_api.permissions import IsOwnerOrReadOnly
# from project_api.serializers import LikeSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.RegisterSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostListView(generics.ListAPIView):
    #Endpoint for retrieve all posts
    queryset = Post.objects.select_related('owner',  )
    serializer_class = serializers.PostSerializer
    filter_by = (filters.DjangoFilterBackend, )
    filterset_fields = ('title',)

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        print(f'Queries counted: {len(connection.queries)} ') #подсчет запросов
        return response

class PostCreateView(generics.CreateAPIView):
    serializer_class = serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetailView(generics.RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )

class LikeCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DisLikeCreateView(generics.ListCreateAPIView):
    queryset = DisLike.objects.all()
    serializer_class = serializers.DisLikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)