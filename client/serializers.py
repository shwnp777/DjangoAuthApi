from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import ClientModel, NotesModel
from profiles.serializers import UserSerializer


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ClientModel
        fields = '__all__'


class NotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = NotesModel
        fields = '__all__'
