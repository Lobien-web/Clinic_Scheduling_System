from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def Homepage(request):
    return render(request, 'homepage.html',{'name':'stunna'})

@login_required
def doctor_dashboard(request):
    if not request.user.groups.filter(name="Doctor").exists():
        return redirect("patient_dashboard")
    return render(request, "doc_dashboard.html")


@login_required
def patient_dashboard(request):
    if request.user.groups.filter(name="Doctor").exists():
        return redirect("doctor_dashboard")
    return render(request, "dashboard.html")
