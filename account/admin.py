from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
