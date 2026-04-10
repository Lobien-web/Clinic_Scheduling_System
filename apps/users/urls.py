from django.urls import path
from . import views
from .views import CustomLoginView, register_Landing

urlpatterns = [
    path("dashboard/", views.dashboard_redirect, name="dashboard"),
    path("dashboard/patient/", views.patient_dashboard, name="patient_dashboard"),
    path("dashboard/doctor/", views.doctor_dashboard, name="doctor_dashboard"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("registerlanding/", register_Landing, name="registerlanding"),
]
