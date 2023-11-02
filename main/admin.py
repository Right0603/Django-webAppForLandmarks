from django.contrib import admin


# Register your models here.

from .models import *


admin.site.register(Category)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=("title", "category", "author", "pub_date")

admin.site.register(Image)

#Parole - d4tapusi
