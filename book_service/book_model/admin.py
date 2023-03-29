from django.contrib import admin

# Register your models here.
from .models.book import Book

admin.site.register(Book)