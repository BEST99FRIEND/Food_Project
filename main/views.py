from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render

from main.forms import ProductForm
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


def add_product(request: WSGIRequest):
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            product= form.save()
            return redirect('index')

    form = ProductForm()
    context = {
        'form': form
    }

    return render(request, template_name='main/add_product.html', context=context)