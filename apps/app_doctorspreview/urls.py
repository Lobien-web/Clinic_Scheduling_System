from django.urls import path
from . import views

urlpatterns = [
    path('doctors',views.DoctorList, name='doctor list'),
]
