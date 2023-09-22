from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<int:article_id>/", views.article, name="article"),
    path("create/", views.create, name="create"),
    path("aboutUs/", views.about_us, name="aboutUs"),
]