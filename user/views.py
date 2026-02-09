from django.shortcuts import redirect, render, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_view(request: WSGIRequest):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Ro'yxatdan o'tish muvaffaqiyatli. Endi tizimga kiring.")
            return redirect('index')
        messages.error(request, "Ro'yxatdan o'tishda xatolik bor. Iltimos, maydonlarni tekshiring.")
    else:
        form = RegisterForm()
    context = {
        "form": form
    }
    return render(request, template_name='user/register.html', context=context)

def login_view(request: WSGIRequest):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Siz tizimga kirdingiz.")
            return redirect('index')
        messages.error(request, "Login yoki parol noto'g'ri.")
    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, template_name='user/login.html', context=context)

def logout_view(request: WSGIRequest):
    logout(request)
    messages.info(request, "Siz tizimdan chiqdingiz.")
    return redirect('login')

@login_required
def user_profile(request: WSGIRequest, username: str):
    user = get_object_or_404(User, username=username)
    context = {
        "user": user
    }
    return render(request, template_name='user/profile.html', context=context)


