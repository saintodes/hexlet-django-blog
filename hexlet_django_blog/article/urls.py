from django.urls import path
from hexlet_django_blog.article.views import IndexView, redirect_to_article


urlpatterns = [
    path("articles/<str:tags>/<int:article_id>", IndexView.as_view(), name="article"),
    path("", redirect_to_article, name="home"),
]
