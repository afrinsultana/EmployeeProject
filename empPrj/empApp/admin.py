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
    list_filter=['department',]
    list_display=('id','name','email','dob','salary','department',)
    search_fields=['email','name','salary','id',]
    list_per_page=4

    resource_class=EmployeeResource

class DepartmentAdmin(admin.ModelAdmin):
    list_filter=['slug',]
    list_display=('id','name','slug',)
    search_fields=['name',]
    list_per_page=3

    prepopulated_fields={'slug':('name', )}
    
    
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department,DepartmentAdmin)


