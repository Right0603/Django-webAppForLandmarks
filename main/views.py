from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        "text": "This is start page!",
    }
    return render(request, "startPage.html", context=data );
