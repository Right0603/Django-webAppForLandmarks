from rest_framework import serializers
from .models import Article

class ArticleSerialization(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'text', 'category', 'Author', 'pub_date']
