from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from urllib3 import request
from apps.users.models import PatientProfile, DoctorProfile
from .models import SpecializationListModel


WEEKDAYS = [
    ("mon", "Monday"),
    ("tue", "Tuesday"),
    ("wed", "Wednesday"),
    ("thu", "Thursday"),
    ("fri", "Friday"),
    ("sat", "Saturday"),
    ("sun", "Sunday"),
]

def RegisterPage(request):
    return render(request, "register.html")

def RegisterPageDoctor(request):
    specialty = SpecializationListModel.objects.all()
    return render(request, "register_doctor.html", {"specialty": specialty
                                                    ,"available_days": WEEKDAYS})

def PushRegisterPage(request):
    
    if request.method != "POST":
        return render(request, "register.html")

    username = request.POST.get("username", "").strip()
    password = request.POST.get("password", "")
    password_conf = request.POST.get("password_conf", "")
    email = request.POST.get("email", "").strip()
    firstname = request.POST.get("firstname", "")
    lastname = request.POST.get("lastname", "")
    pat_name = firstname + " " + lastname
    age = request.POST.get("age", "")
    pat_img = request.FILES.get("pat_img")

    if not username or not email or not password or not password_conf:
        return HttpResponse("All fields are required.", status=400)

    if password != password_conf:
        return HttpResponse("Passwords do not match.", status=400)

    if User.objects.filter(username=username).exists():
        return HttpResponse("Username already taken.", status=400)

    if User.objects.filter(email=email).exists():
        return HttpResponse("Email already registered.", status=400)
    
    if pat_name == "" or age == "":
        return HttpResponse("Missing required fields.", status=400) 
    

    user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
    PatientProfile.objects.create(
        pat_user = user,
        pat_name = pat_name,
        pat_age = age,
        pat_img = pat_img,
    )

    patient_group, _ = Group.objects.get_or_create(name="Patient")
    user.groups.add(patient_group)

    return redirect("login")


def PushRegisterPageDoctor(request):
    if request.method != "POST":
        return render(request, "register_doctor.html")

    username = request.POST.get("username", "").strip()
    password = request.POST.get("password", "")
    password_conf = request.POST.get("password_conf", "")
    email = request.POST.get("email", "").strip()
    firstname = request.POST.get("firstname", "")
    lastname = request.POST.get("lastname", "")
    doctor_name = firstname + " " + lastname
    doctor_age = request.POST.get("doctor_age", "")
    doctor_role = request.POST.get("doctor_role", "")
    doctor_available_days = request.POST.getlist("doctor_available_days", [])
    doctor_schedule_time_start = request.POST.get("doctor_schedule_time_start", "")
    doctor_schedule_time_end = request.POST.get("doctor_schedule_time_end", "")
    doctor_img = request.FILES.get("doctor_img")
    clinic_name = request.POST.get("clinic_name", "")
    lat = request.POST.get("clinic_latitude")
    lng = request.POST.get("clinic_longitude")
    
    if not username or not email or not password or not password_conf:
        return HttpResponse("All fields are required.", status=400)

    if password != password_conf:
        return HttpResponse("Passwords do not match.", status=400)
    
    if doctor_name == "" or doctor_age == "" or doctor_role == "":
        return HttpResponse("Missing required fields.", status=400)

    if User.objects.filter(username=username).exists():
        return HttpResponse("Username already taken.", status=400)

    if User.objects.filter(email=email).exists():
        return HttpResponse("Email already registered.", status=400)
    
    if clinic_name == "":
        return HttpResponse("Clinic name is required.", status=400)

    if  lat == "" or lng == "":
        return HttpResponse("Clinic location not selected.", status=400)
    
    user = User.objects.create_user(username=username,
                                     email=email,
                                       password=password,
                                         first_name=firstname,
                                           last_name=lastname,
                                             )
    DoctorProfile.objects.create(
        doctor_user = user,
        doctor_name = doctor_name,  
        doctor_age = doctor_age,
        doctor_role = doctor_role,
        doctor_available_days = doctor_available_days,
        doctor_schedule_time_start = doctor_schedule_time_start,
        doctor_schedule_time_end = doctor_schedule_time_end,
        doctor_img = doctor_img,
        clinic_latitude = float(lat) if lat else 0.0,
        clinic_longitude = float(lng) if lng else 0.0
    )
    
    doctor_group, _ = Group.objects.get_or_create(name="Doctor")
    user.groups.add(doctor_group)

    return redirect("login")


