from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import *

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html" 


class EmployeeListView(ListView):
    model = Employee
    template_name = "emp/list.html"
    paginate_by=2
