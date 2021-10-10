from django.urls import path, include
from .views import ListEmployeesView,CreateEmployeesView

urlpatterns = [
    path('employees_create/', CreateEmployeesView.as_view(), name='employees_create'),
    path('employees_list/', ListEmployeesView.as_view(), name='employees_list'),
]
