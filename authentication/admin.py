from django.contrib import admin
from django.contrib import admin
from .models.unilever_user import UnileverUser


# Register your models here.

class UnileverUserAdmin(admin.ModelAdmin):
    model = UnileverUser


admin.site.register(UnileverUser, UnileverUserAdmin)
