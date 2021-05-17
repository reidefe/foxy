from django.shortcuts import render
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from .permisions import IsOwnerProfileOrReadOnly
from .serializers import UserSerializer, NewsSerializer
from .models import UserModel, NewsModel
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = NewsModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

   


class UserProfileListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerProfileOrReadOnly)
