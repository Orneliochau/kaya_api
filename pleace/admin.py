from django.contrib import admin
from pleace.models import PleaceInformation, Employee, department_id


class PleaceAdmin(admin.ModelAdmin):
    list_display = ['place_name']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name']

admin.site.register(department_id)

admin.site.register(PleaceInformation, PleaceAdmin)

admin.site.register(Employee, EmployeeAdmin)
# Register your models here.
