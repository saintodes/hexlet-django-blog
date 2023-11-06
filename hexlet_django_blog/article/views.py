from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponse


class IndexView(View):
    def get(self, request, tags, article_id, *args, **kwargs):
        return HttpResponse(f"Статья номер {article_id}. Тег {tags}")


def redirect_to_article(request):
    article_url = reverse("article", kwargs={"tags": "python", "article_id": 42})
    return redirect(article_url)
