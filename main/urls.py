from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<int:article_id>/", views.article, name="article"),
    path("create/", views.create_article, name="create"),
    path("aboutUs/", views.about_us, name="aboutUs"),
    path("sign-up/", views.sign_up, name="sign-up"),
    path('articles/', views.ArticleListAPI),
    path("edit/<int:article_id>/", views.edit_article, name="edit"),
    path("delete/<int:article_id>/", views.delete_article, name="delete"),
]