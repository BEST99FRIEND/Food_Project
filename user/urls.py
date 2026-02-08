from django.urls import path, include
from user import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
]
