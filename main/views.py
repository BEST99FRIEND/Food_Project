from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from . models import HeroSlider

def index(request: WSGIRequest):
    sliders = HeroSlider.objects.filter(published=True)
    context = {
        'title': 'Home Page',
    }
    return render(request, template_name='index.html', context=context)