from django.shortcuts import render

def index(request):
    context = {
        'app_name': 'Hexlet Django Blog',
    }
    return render(request, 'articles/index.html', context)
