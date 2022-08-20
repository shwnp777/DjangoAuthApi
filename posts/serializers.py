from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import PostModel, ReplyModel
from profiles.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = PostModel
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = ReplyModel
        fields = '__all__'
