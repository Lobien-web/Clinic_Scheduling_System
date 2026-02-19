from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ScheduleInfo
from apps.users.services import get_doctor


# Create your views here.

def SetSchedule(request):
    doctors = get_doctor()
    return render(request, 'appointment.html',{"doctor": doctors})

def PushSchedule(request):
    doctors = get_doctor()
    if request.method != "POST":
        return redirect("Set_schedule")
    
    doctor_id = request.POST.get("doctor") 
    date = request.POST.get("sched_date")
    time = request.POST.get("sched_time")

    if doctor_id and date and time:
        ScheduleInfo.objects.create(
            sched_doctor_id=doctor_id,
            sched_date = date,
            sched_time = time,
        )
        return redirect("Set_schedule")
    
    