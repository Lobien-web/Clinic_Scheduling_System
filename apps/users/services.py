from .models import DoctorProfile, PatientProfile

def get_doctor():
    return DoctorProfile.objects.all()

def get_patient():
    return PatientProfile.objects.all()