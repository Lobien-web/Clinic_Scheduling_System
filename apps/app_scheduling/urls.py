from django.urls import path
from . import views

urlpatterns = [
    path('Set_schedule/',views.SetSchedule, name='Set_schedule'),
    path('PushSchedule/', views.PushSchedule, name='Push_schedule')
]
