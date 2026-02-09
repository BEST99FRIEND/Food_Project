from django.shortcuts import redirect, render
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404
from main.forms import ProductForm
from django.contrib.auth.models import User
from .forms import AuthenticationForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout

def register_view(request: WSGIRequest):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('index')
    context = {
        "form":RegisterForm()
    }
    return render(request, template_name='user/register.html', context=context)

def login_view(request: WSGIRequest):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print('Siz tizimga kirdingiz')
            return redirect('index')

    context = {
        "form": LoginForm()
    }
    return render(request, template_name='user/login.html', context=context)

def logout_view(request: WSGIRequest):
    logout(request)
    print('Siz tizimdan chiqdingiz')
    return redirect('login')

def user_profile(request: WSGIRequest, username: str):
    user = get_object_or_404(User, username=username)
    context = {
        "user": user
    }
    return render(request, template_name='user/profile.html', context=context)




# if request.POST.get('password1') == request.POST.get('password2'):
#     user = User.objects.create_user(
#         username=request.POST.get('username'),
#         email=request.POST.get('email'),
#         password=request.POST.get('password1')
#     )
#     print('Siz royhatdan otdingiz')
#     return redirect('index') 