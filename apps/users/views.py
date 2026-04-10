from inspect import ismethod

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from requests import request
from .models import DoctorProfile, PatientProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from apps.app_scheduling.models import ScheduleInfo

# Create your views here.

def doctor_li(request):
      
      doctor_li = DoctorProfile.objects.all()
      return render(request, "")

from django.shortcuts import redirect

def dashboard_redirect(request):
    
    if request.user.groups.filter(name="Doctor").exists():
        return redirect("doctor_dashboard")
    else:
        return redirect("patient_dashboard")
    
def register_Landing(request):
    return render(request, "register_initial.html")

class CustomLoginView(LoginView):
    template_name = "login.html"
    authentication_form = CustomLoginForm






@login_required
def patient_dashboard(request):
    return render(request, "dashboard.html")

@login_required
def doctor_dashboard(request):
    doctor_profile = DoctorProfile.objects.filter(doctor_user=request.user).first()
    schedules = ScheduleInfo.objects.filter(sched_doctor=doctor_profile,
        sched_status=False)

    schedulesAccepted = ScheduleInfo.objects.filter(
        
        sched_doctor=doctor_profile,
        sched_status=True,
        sched_status_complete=False)
    
    schedulesCompleted = ScheduleInfo.objects.filter(
        
        sched_doctor=doctor_profile,
        sched_status=True,
        sched_status_complete=True
    )
    return render(request, "doc_dashboard.html",{
        "schedules" : schedules,
        "schedulesAccepted": schedulesAccepted,
        "schedulesCompleted": schedulesCompleted
    })


@login_required
def approve_or_reject(request, schedule_id):
    if request.method != "POST":
        return redirect("doctor_dashboard")  # change to your page name

    sched = get_object_or_404(ScheduleInfo, id=schedule_id)
    action = request.POST.get("action")

    if action == "approve":
        sched.sched_status = True
        sched.save()

    elif action == "cancel":
        sched.sched_status = False
        sched.sched_status_complete = False  # optional: cancel also un-completes
        sched.save()

    elif action == "complete":
        # only allow complete if approved
        if sched.sched_status:
            sched.sched_status_complete = True
            sched.save()

    return redirect("doctor_dashboard")  # same page where schedules are liste


@login_required
def completeSched(request, schedule_id):
    if request.method == "POST":
        schedule = request.POST.get("schedule_id") or ScheduleInfo.objects.get(id=schedule_id)
        schedule.sched_status_complete = not schedule.sched_status_complete
        print(schedule.sched_status_complete)
        schedule.save()
        
        return redirect("doctor_dashboard")       