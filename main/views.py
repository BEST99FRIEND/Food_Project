from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render, get_object_or_404
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
        print(request.FILES)
        if form.is_valid():
            product= form.save()
            return redirect('index')

    form = ProductForm()
    context = {
        'form': form
    }

    return render(request, template_name='main/add_product.html', context=context)

def product_detail(request: WSGIRequest, pk: int):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, template_name='main/detail.html', context=context)

def product_update(request: WSGIRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        print(request.POST)
        form = ProductForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)

    form = ProductForm(instance=product)
    context = {
        "product": product,
        'form': form
    }
    return render(request, template_name='main/add_product.html', context=context)

def product_delete(request: WSGIRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('index')

    context = {
        "product": product
    }
    return render(request, template_name='main/product_delete.html', context=context)