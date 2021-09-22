from django.urls import path
from . import views

app_name='utilApp'

urlpatterns = [
    
     path('sendmail/',views.SendEmailwithAttachment,name='sendmail'),
    # path('delete/<int:pk>',views.EmployeeDeleteView.as_view(),name='delete'),

]