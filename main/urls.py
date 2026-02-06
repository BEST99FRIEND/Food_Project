from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_product, name='add_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('update/<int:pk>/', views.product_update, name='product_update'),
]
