from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import BusinessModel
from .serializers import BusinessSerializer


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = BusinessModel.objects.all()
    serializer_class = BusinessSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)



