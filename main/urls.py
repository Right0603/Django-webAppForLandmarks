from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<int:article_id>/", views.article, name="article"),
    path("create/", views.create_article, name="create"),
    path("aboutUs/", views.about_us, name="about-us"),
    path("sign-up/", views.sign_up, name="sign-up"),
    path('articles/', views.ArticleListAPI),
    path("edit/<int:article_id>/", views.edit_article, name="edit"),
    path("delete/<int:article_id>/", views.delete_article, name="delete"),
    path("museums/", views.museums_category, name="museums"),
    path("parks/", views.parks_category, name="parks"),
    path("lakes/", views.lakes_category, name="lakes"),
    path("churches/", views.churches_category, name="churches"),
    path("other/", views.other_category, name="other"),
]