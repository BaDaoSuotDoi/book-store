from django.contrib import admin

# Register your models here.
from .models.cart import Cart

admin.site.register(Cart)