from empPrj.empApp.models import Department
from django.contrib import admin
from empApp.models import Employee

from import_export import resources
from import_export.admin import ImportExportMixin

# Register your models here.

class EmployeeResource(resources.ModelResource):
    class Meta:
        model=Employee
        exclude=('photo',)

class EmployeeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_filter=['department']
    list_display=('name','email','dob','salary','department',)
    resource_class=EmployeeResource

admin.site.register(Employee,EmployeeAdmin)

