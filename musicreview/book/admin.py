from django.contrib import admin
from .models import Book2, Book3


@admin.register(Book2)
class Book2Admin(admin.ModelAdmin):
    list_display = 'pk', 'author', 'subject'
    list_display_links = ['author']
    ordering = ['-pk']


@admin.register(Book3)
class Book3Admin(admin.ModelAdmin):
    list_display = 'pk', 'author', 'subject'
    list_display_links = ['author']
    ordering = ['-pk']
