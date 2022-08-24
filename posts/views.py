from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import PostModel, ReplyModel
from .serializers import PostSerializer, ReplySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = PostModel.objects.all().order_by('created_at')
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = ReplyModel.objects.all().order_by('created_at')
    serializer_class = ReplySerializer
