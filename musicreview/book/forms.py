from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

from .models import Book2, Book3


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ("username", "email")


class Book2Form(ModelForm):
    class Meta:
        model = Book2
        fields = ("subject", "full_text", "author")

        widgets = {
            "subject":  TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'

            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор',
                'value': 'request.user.id'
            }),

        }


class Book3Form(ModelForm):
    class Meta:
        model = Book3
        fields = ("subject", "full_text", "author")

        widgets = {
            "subject":  TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'

            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор',
                'initial': 1
            }),

        }


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ("username", "password")
