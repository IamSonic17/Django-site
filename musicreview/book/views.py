from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Book
from django import forms


def book_home(request):
    mes = Book.objects.order_by('-date')
    return render(request, template_name='book/book_home.html', context={'mes': mes})


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ("username", "email")
        #field_classes = {"username": UsernameField}


def register_new_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "book/user_register_done.html")
    else:
        form = RegistrationForm()

    return render(request, "book/user_register_form.html", context={"form": form})


def add_message_view(request):
    if request.method == 'POST':
        if 'subject' in request.POST:
            subj = request.POST['subject']
        else:
            subj = "Пусто"

