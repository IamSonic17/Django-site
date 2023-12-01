from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = 'pk', 'author', 'subject', 'date'
    list_display_links = ['author']
    ordering = ['-pk']

