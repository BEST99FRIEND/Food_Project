from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from main.forms import ProductForm
from . models import Category, HeroSlider, Product

def index(request: WSGIRequest):
    sliders = HeroSlider.objects.filter(published=True)
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)[:9]
    discounted_products = (
        Product.objects
        .filter(is_active=True, discount__gt=0)
        .order_by('-discount', '-created_at')[:2]
    )
    context = {
        'title': 'Home Page',
        'sliders': sliders,
        'categories': categories,
        'products': products,
        'discounted_products': discounted_products,
    }
    return render(request, template_name='index.html', context=context)


@login_required
@permission_required('main.add_product', raise_exception=True)
def add_product(request: WSGIRequest):
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Mahsulot muvaffaqiyatli qo'shildi.")
            return redirect('index')
        messages.error(request, "Mahsulot qo'shishda xatolik bor. Maydonlarni tekshiring.")
    else:
        form = ProductForm()

    context = {
        'form': form
    }

    return render(request, template_name='main/add_product.html', context=context)

def product_detail(request: WSGIRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, template_name='main/detail.html', context=context)

@login_required
@permission_required('main.change_product', raise_exception=True)
def product_update(request: WSGIRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Mahsulot muvaffaqiyatli yangilandi.")
            return redirect('product_detail', pk=product.pk)
        messages.error(request, "Mahsulotni yangilashda xatolik bor. Maydonlarni tekshiring.")
    else:
        form = ProductForm(instance=product)
    context = {
        "product": product,
        'form': form
    }
    return render(request, template_name='main/add_product.html', context=context)

@login_required
@permission_required('main.delete_product', raise_exception=True)
def product_delete(request: WSGIRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Mahsulot o'chirildi.")
        return redirect('index')

    context = {
        "product": product
    }
    return render(request, template_name='main/confirm_delete.html', context=context)
