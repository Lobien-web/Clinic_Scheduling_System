from django.urls import path
from . import views

urlpatterns = [
    path('',views.Homepage, name='homepage'),
    path("dashboard/doctor/", views.doctor_dashboard, name="doctor_dashboard"),
    path("dashboard/patient/", views.patient_dashboard, name="patient_dashboard"),
]
