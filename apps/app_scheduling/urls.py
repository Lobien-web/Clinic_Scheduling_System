from django.urls import path
from . import views

urlpatterns = [
    path('set_schedule/',views.set_schedule, name='set_schedule'),
    path('push_schedule/', views.push_schedule, name='push_schedule')
    
]
