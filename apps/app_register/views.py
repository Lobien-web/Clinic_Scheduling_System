from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from apps.users.models import PatientProfile

def RegisterPage(request):
    return render(request, "register.html")

def RegisterPageDoctor(request):
    return render(request, "register_doctor.html")

def PushRegisterPage(request):
    if request.method != "POST":
        return render(request, "register.html")

    username = request.POST.get("username", "").strip()
    password = request.POST.get("password", "")
    password_conf = request.POST.get("password_conf", "")
    email = request.POST.get("email", "").strip()

    if not username or not email or not password or not password_conf:
        return HttpResponse("All fields are required.", status=400)

    if password != password_conf:
        return HttpResponse("Passwords do not match.", status=400)

    if User.objects.filter(username=username).exists():
        return HttpResponse("Username already taken.", status=400)

    if User.objects.filter(email=email).exists():
        return HttpResponse("Email already registered.", status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    profile = PatientProfile.objects.create(pat_user=user)

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

    if not username or not email or not password or not password_conf:
        return HttpResponse("All fields are required.", status=400)

    if password != password_conf:
        return HttpResponse("Passwords do not match.", status=400)

    if User.objects.filter(username=username).exists():
        return HttpResponse("Username already taken.", status=400)

    if User.objects.filter(email=email).exists():
        return HttpResponse("Email already registered.", status=400)

    user = User.objects.create_user(username=username, email=email, password=password)

    doctor_group, _ = Group.objects.get_or_create(name="Doctor")
    user.groups.add(doctor_group)

    return redirect("login")
