from django.urls import path
from main import views
from .views import index, add_product

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_product, name='add_product'),
]
