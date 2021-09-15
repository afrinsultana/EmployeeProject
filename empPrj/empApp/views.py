from django.shortcuts import render
from django.urls.base import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import *
from django.urls import reverse

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html" 


class EmployeeListView(ListView):
    model = Employee
    template_name = "emp/list.html"
    # paginate_by=2


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "emp/empForm.html"
    form_class=EmployeeForm

    def get_success_url(self):
        return reverse('employee:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] ='Create' 
        context["heading"] ='Create New Employee' 
        return context
    

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "emp/empForm.html"
    form_class=EmployeeForm
    success_url=reverse_lazy('employee:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit'
        context["heading"]='Update Employee'
        return context
    


