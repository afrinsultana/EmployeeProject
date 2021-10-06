from django.urls import path
from utilApp import views

app_name='utilApp'

urlpatterns = [
    
     path('sendmail/',views.SendEmailwithAttachment,name='sendmail'),
    # path('delete/<int:pk>',views.EmployeeDeleteView.as_view(),name='delete'),
     path('csv/',views.export_employee_csv,name='export_employee_csv'),
     path('about/',views.AboutView.as_view(),name='about'),
     path('group_by_dept/',views.group_by_dept,name='group_by_dept'),
     path('showchart/<str:chartType>',views.show_chart,name='mouChart'),

]