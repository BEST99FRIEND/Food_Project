from django.shortcuts import redirect, render
from django.core.handlers.wsgi import WSGIRequest

def register_view(request: WSGIRequest):
    if request.method == 'POST':
        print(request.POST)
        # Bu yerda foydalanuvchi ma'lumotlarini qayta ishlash va ro'yxatdan o'tkazish logikasini qo'shishingiz mumkin
        return redirect('index')  # Ro'yxatdan o'tgandan so'ng, foydalanuvchini bosh sahifaga yo'naltirish
    return render(request, template_name='user/register.html')