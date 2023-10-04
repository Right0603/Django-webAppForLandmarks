from django.contrib import admin

from main.forms import ArticleForm

# Register your models here.

from .models import Article, Category


admin.site.register(Category)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    def save_model(self, request, obj, form, change):
        obj.Author = request.user
        super().save_model(request, obj, form, change)

#Parole - d4tapusi
