from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.users.models import PatientProfile
from .models import ScheduleInfo
# from apps.users.services import get_doctor
from apps.users import views, services




# Create your views here.

def set_schedule(request):
    doctors = views.DoctorProfile.objects.all()
    return render(request, 'appointment.html',{"doctor": doctors})

def push_schedule(request):  
    
    
    doctors = services.get_doctor()
    if request.method != "POST":
        return redirect("set_schedule")
    
    doctor_id = request.POST.get("doctor") 
    date = request.POST.get("sched_date")
    time = request.POST.get("sched_time")

    if doctor_id == "Select Doctor" or date == "" or time == "":
        return HttpResponse("All fields are required.", status=400)
    
    try:
        patient = views.PatientProfile.objects.get(pat_user=request.user)
    except views.PatientProfile.DoesNotExist:
        return HttpResponse("Patient not found.", status=400)
    
    ScheduleInfo.objects.create(
            sched_doctor_id=doctor_id,
            sched_img = patient.pat_img,
            sched_patient = patient,
            sched_date = date,
            sched_time = time,  
        )
    return redirect("set_schedule")