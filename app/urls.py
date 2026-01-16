from django.urls import path
from .views import *

urlpatterns = [

    path("root/", root, name="root"),
    
    path("employees/", employee_list_create, name="employee_list_create"),
    path("employees/<int:pk>/", employee_detail, name="employee_detail"),
]
