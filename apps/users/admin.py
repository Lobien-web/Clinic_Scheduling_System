from django.contrib import admin
from .models import DoctorProfile, PatientProfile

admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)

