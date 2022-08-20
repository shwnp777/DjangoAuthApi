from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import BusinessModel


class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessModel
        fields = '__all__'


