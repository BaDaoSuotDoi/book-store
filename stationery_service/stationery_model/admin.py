from django.contrib import admin

# Register your models here.
from .models.stationery import Stationery

admin.site.register(Stationery)