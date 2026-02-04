from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from . models import Category, HeroSlider, Product

def index(request: WSGIRequest):
    sliders = HeroSlider.objects.filter(published=True)
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)[:9]
    context = {
        'title': 'Home Page',
        'sliders': sliders,
        'categories': categories,
        'products': products
    }
    return render(request, template_name='index.html', context=context)