from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        "text": "This is start page!",
    }

    return render(request, "startPage.html", context=data )


def article(request, article_id):
    data = {
        "text": f"This is article number {article_id}"
    }
    return render(request, "article.html", context=data )

def create(request):
    return render(request, "createArticle.html")

def about_us(request):
    return render(request, "aboutUs.html")