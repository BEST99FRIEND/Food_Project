from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'image', 'is_active']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'price': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'category': forms.Select(attrs={'class': 'form-control'}),
        #     'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        #     'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        # }
