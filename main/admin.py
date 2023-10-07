from django.contrib import admin

from main.forms import ArticleForm

# Register your models here.

from .models import Article, Category, Image


admin.site.register(Category)

admin.site.register(Article)

admin.site.register(Image)

#Parole - d4tapusi
