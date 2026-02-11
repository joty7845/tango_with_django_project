from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'crash course to Django'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse(
        "Rango says here is the about page. "
        "<a href='/rango/'>Index</a>"
    )