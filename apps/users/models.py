from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DoctorProfile(models.Model):
    doctor_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,  blank=True)
    doctor_name = models.CharField(max_length=200,default="")
    doctor_age = models.IntegerField()
    doctor_role = models.CharField(max_length=100,default="")
    doctor_schedule_date_begin = models.DateField((""), auto_now=False, auto_now_add=False)
    doctor_schedule_date_end = models.DateField((""), auto_now=False, auto_now_add=False)
    doctor_schedule_time            = models.TimeField((""), auto_now=False, auto_now_add=False)
    doctor_img = models.ImageField(upload_to="doctors/", blank=True, null=True, default="")

    def __str__(self):
        return self.doctor_name



class PatientProfile(models.Model):
    pat_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,  blank=True)
    pat_doctor = models.ForeignKey(DoctorProfile,on_delete=models.SET_NULL,null=True,blank=True)
    pat_name = models.CharField(max_length=200)
    pat_age = models.IntegerField()
    pat_recentSched = models.DateTimeField(blank=True, null=True)
    schedule_req_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.pat_name