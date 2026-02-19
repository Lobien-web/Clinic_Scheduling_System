from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterPage, name='RegistrationPage'),
    path('registerdoctor/',views.RegisterPageDoctor, name='RegistrationPageDoctor'),
    path('PushRegisterPage/', views.PushRegisterPage, name='PushRegisterPage'),
    path('PushRegisterPageDoctor/', views.PushRegisterPageDoctor, name='PushRegisterPageDoctor'),
]
