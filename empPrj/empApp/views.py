from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import *
from django.urls import reverse
from django.contrib import messages

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html" 


# class EmployeeListView(ListView):
#     model = Employee
#     template_name = "emp/list.html"
#     # paginate_by=2


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "emp/empForm.html"
    form_class=EmployeeForm

    def get_success_url(self):
        messages.success(self.request,'Data Inserted Successfully...')
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
    # success_url=reverse_lazy('employee:list')

    def get_success_url(self):
        messages.success(self.request,'Data Updated Successfully...')
        return reverse('employee:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit'
        context["heading"]='Update Employee'
        return context
    

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "emp/delete.html"
    form_class=EmployeeForm

    def get_success_url(self):
        messages.success(self.request,'Data Deleted Successfully...')
        return reverse('employee:list')


def employee_list(request,department_slug=None):
    department=None
    departments=Department.objects.all()
    employees=Employee.objects.all()
    if department_slug:
        department=get_object_or_404(Department,slug=department_slug)
        employees=Employee.objects.filter(department=department)
        
    context={'department':department,'departments':departments,'object_list':employees}
    return render(request,'emp/list.html',context)
        

