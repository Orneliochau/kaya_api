from django.contrib import admin
from place.models import PleaceInformation, placeImages


class PleaceAdmin(admin.ModelAdmin):
    list_display = ['place_name']




admin.site.register(PleaceInformation, PleaceAdmin)

admin.site.register(placeImages)

# Register your models here.
