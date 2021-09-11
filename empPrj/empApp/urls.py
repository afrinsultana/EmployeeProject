from django.urls import path
from . import views

app_name='empApp'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('list/',views.EmployeeListView.as_view(),name='list'),
]