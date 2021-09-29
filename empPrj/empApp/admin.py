from django.contrib import admin
from .models import *

from import_export import resources
from import_export.admin import ImportExportMixin

# Register your models here.

class EmployeeResource(resources.ModelResource):
    class Meta:
        model=Employee
        exclude=('photo','created_at','updated_at',)

class EmployeeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_filter=['department']
    list_display=('name','email','dob','salary','department',)
    resource_class=EmployeeResource

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department)


