from django.contrib import admin
from pleace.models import PleaceInformation

admin.site.register(PleaceInformation)
class PleaceAdmin(admin.ModelAdmin):
    list_display = ['place_name']
# Register your models here.
