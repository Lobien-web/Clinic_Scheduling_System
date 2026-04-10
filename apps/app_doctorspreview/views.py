from django.shortcuts import render
from apps.users.models import DoctorProfile
# Create your views here.
def DoctorList(request):
    doctors = DoctorProfile.objects.all()
    return render(request, 'doctors_list.html', {"DoctorList": doctors})
    