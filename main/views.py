from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

def index(request: WSGIRequest):
    context = {
        'title': 'Home Page',
    }
    return render(request, template_name='index.html', context=context)