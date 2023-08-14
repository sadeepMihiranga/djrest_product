from django.contrib import admin
from django.contrib import admin
from .models import UnileverUser


# Register your models here.

class UnileverUserAdmin(admin.ModelAdmin):
    model = UnileverUser


admin.site.register(UnileverUser, UnileverUserAdmin)
