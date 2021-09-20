from django.urls import path
from . import views

app_name='empApp'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    # path('list/',views.EmployeeListView.as_view(),name='list'),
    path('create/',views.EmployeeCreateView.as_view(),name='create'),
    path('update/<int:pk>',views.EmployeeUpdateView.as_view(),name='update'),
    path('list/<str:department_slug>/',views.employee_list,name='emplist_by_department'),
    path('show/',views.employee_list,name='list'),
    path('delete/<int:pk>',views.EmployeeDeleteView.as_view(),name='delete'),

]