from django.shortcuts import render
from django.http import HttpResponse
from .models import DoctorProfile, PatientProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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


@login_required
def patient_dashboard(request):
    return render(request, "dashboard.html")

@login_required
def doctor_dashboard(request):
    return render(request, "doc_dashboard.html")