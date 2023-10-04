from rest_framework import serializers
from .models import Article

class ArticleSerialization(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'text', 'pub_date']
