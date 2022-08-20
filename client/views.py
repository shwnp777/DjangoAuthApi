from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import ClientModel, NotesModel
from .serializers import ClientSerializer, NotesSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)


class NotesViewSet(viewsets.ModelViewSet):
    queryset = NotesModel.objects.all()
    serializer_class = NotesSerializer
