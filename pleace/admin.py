from django.contrib import admin
from pleace.models import PleaceInformation, Employee, department_id

admin.site.register(PleaceInformation)
class PleaceAdmin(admin.ModelAdmin):
    list_display = ['place_name']

admin.site.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name']

admin.site.register(department_id)
# Register your models here.
