from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(sel, request, *args, **kwargs):
        return render(
            request,
            "articles/index.html",
            context={
                "app_name": "Hexlet Django Blog",
            },
        )
