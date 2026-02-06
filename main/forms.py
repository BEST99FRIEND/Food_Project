from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'image', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'title': 'Nomi',
            'description': 'Tavsif',
            'price': 'Narx',
            'category': 'Kategoriya',
            'image': 'Rasm',
            'is_active': 'Faol',
        }
        help_texts = {
            'title': 'Mahsulot nomini kiriting',
            'description': 'Mahsulot tavsifini kiriting',
            'price': 'Mahsulot narxini kiriting',
            'category': 'Mahsulot kategoriyasini tanlang',
            'image': 'Mahsulot rasmini yuklang',
        }
        error_messages = {
            'title': {
                'required': 'Mahsulot nomini kiriting!',
                'max_length': 'Mahsulot nomi 100 belgidan oshmasligi kerak!',
            },
            'description': {
                'required': 'Mahsulot tavsifini kiriting!',
            },
            'price': {
                'required': 'Mahsulot narxini kiriting!',
                'invalid': 'Narx noto\'g\'ri formatda!',
            },
            'category': {
                'required': 'Mahsulot kategoriyasini tanlang!',
            },
        }