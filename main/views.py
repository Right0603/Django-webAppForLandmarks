from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):

    return render(request, "startPage.html", {"articles": Article.objects.all()} )


def article(request, article_id):
    data = {
        "text": f"This is article number {article_id}"
    }
    return render(request, "article.html", context=data )

def create(request):
    return render(request, "createArticle.html")

def about_us(request):
    return render(request, "aboutUs.html")