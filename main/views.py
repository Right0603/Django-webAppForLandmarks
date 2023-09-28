from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    return render(request, "startPage.html", {"articles": Article.objects.all()} )


def article(request, article_id):
    data = Article.objects.get(id=article_id)
    return render(request, "article.html", {"article": data})

def create(request):  
    form = ArticleForm() 
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            
    context={'form':form}
    return render(request, "createArticle.html", context)

def about_us(request):
    return render(request, "aboutUs.html")