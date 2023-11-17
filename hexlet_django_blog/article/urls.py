from django.urls import path

from hexlet_django_blog.article.views import IndexView, ArticleFormCreateView, ArticleView, ArticleFormEditView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view()),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
]