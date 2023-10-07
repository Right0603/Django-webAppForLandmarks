from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from .models import Article, Image
from .serialization import ArticleSerialization
from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(request):
    return render(request, "startPage.html", {"articles": Article.objects.all()} )

def about_us(request):
    return render(request, "aboutUs.html")

def article(request, article_id):
    a = Article.objects.get(id=article_id)
    images = Image.objects.filter(article = a)
    return render(request, "article.html", {"article": a, "images": images})


@login_required
def create_article(request):   
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        images = request.FILES.getlist('image')
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            for i in images:
                new_image = Image(image=i, article=article)
                new_image.save()
            return redirect(index)
    else:
        form = ArticleForm()
    return render(request, "createArticle.html", {'form': form})

def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
                article = form.save(commit=False)
                article.author = request.user
                article.save()
                return redirect(index) 

    return render(request, 'editArticle.html', {'article': article})

def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect(index)


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(index)
    else:
        form = RegisterForm()
        
        return render(request, 'registration/sign_up.html', {"form": form})
    
@api_view(['GET'])
def ArticleListAPI(request):
    result = Article.objects.all()
    message = ArticleSerialization(result, many=True)
    return Response(message.data)

