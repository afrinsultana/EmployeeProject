from django import forms
from django.forms import fields
from .models import *

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__' 


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'      