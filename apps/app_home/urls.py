from django.urls import path
from . import views
from apps.users import views as user_views

urlpatterns = [
    path('',views.Homepage, name='homepage'),
    path("dashboard/doctor/", views.doctor_dashboard, name="doctor_dashboard"),
    path("dashboard/patient/", views.patient_dashboard, name="patient_dashboard"),
    path("dashboard/status/<int:schedule_id>/", user_views.approve_or_reject, name="status"),
   
]   