from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django import forms

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=150, label='Username', widget=forms.TextInput(
        attrs={
            "id": "username",
            "name": "username",
            "class": "form-control",
        }
    ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Username', widget=forms.TextInput(
        attrs={
            "id": "username",
            "name": "username",
            "class": "form-control",
        }
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'password': 'password',
            'class': 'form-control'
        }
    ))