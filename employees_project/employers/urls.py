from django.urls import path, include
from .views import ListEmployeesView,CreateEmployeesView,UploadFileView

urlpatterns = [
    path('employees_create/', CreateEmployeesView.as_view(), name='employees_create'),
    path('employees_list/', ListEmployeesView.as_view(), name='employees_list'),
    path('upload-csv/', UploadFileView.as_view(), name='upload-csv'),
]
