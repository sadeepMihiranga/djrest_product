from django.contrib import admin
from .models.product import Product
from .models.keyword import Keyword

# Register your models here.

admin.site.register(Product)
admin.site.register(Keyword)
