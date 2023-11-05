from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
        'app_name' : 'Hexlet Django blog',
    })

def about(request):
    return render(request, 'about.html')