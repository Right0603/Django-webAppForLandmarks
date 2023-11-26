from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= ['title', 'description']

class ArticleSerialization(serializers.ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Article
        fields = ['title', 'text', 'category', 'author']
