from django.urls import path
from .views import EmployeesDetail, EmployeesList


urlpatterns = [
    path("", EmployeesList.as_view(), name="api_list"),
    path("<int:pk>/", EmployeesDetail.as_view(), name=""),
]
