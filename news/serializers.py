from rest_framework import serializers
from .models import UserModel, NewsModel


class UserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserModel
        fields = "__all__"
        ref_name = "User Serializer"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ["heading", "body"]
