from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm, Book2Form, Book3Form, LoginForm
from .models import Book2, Book3
from django.contrib.auth.models import User


def book_home(request):
    mes = Book3.objects.order_by('-pk')
    return render(request, template_name='book/book_home.html', context={'mes': mes})


def register_new_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/book")

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "book/user_register_done.html")
    else:
        form = RegistrationForm()

    return render(request, "book/user_register_form.html", context={"form": form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('book_home')

    if request.method == "POST":
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('book_home')
    else:
        form = LoginForm()

    return render(request, "book/login.html", context={"form": form})


def add_message_view(request):
    user_name = User.objects.filter(pk=request.user.id)
    if request.method == 'POST':
        form = Book3Form(request.POST)
        if request.user.is_authenticated:
            form.data = form.data.copy()
            form.data['author'] = user_name[0]
            if form.is_valid():
                form.save()
            return redirect('book_home')
        else:
            pass

    else:
        form = Book3Form()

    return render(request, "book/add_message_form.html", context={"form": form})
