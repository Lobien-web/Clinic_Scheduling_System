from django.db import models


class ScheduleInfo(models.Model):

    sched_doctor = models.ForeignKey("users.DoctorProfile",on_delete=models.SET_NULL,null=True,blank=True,)
    sched_patient = models.ForeignKey('users.PatientProfile', on_delete=models.CASCADE, blank=True, null=True, default=None)
    sched_date = models.CharField(max_length=200, default="", blank=True)
    sched_time = models.CharField(max_length=20, default="", blank=True)
    sched_status = models.BooleanField(default=False)   

    def __str__(self):

        return f"{self.sched_patient} - {self.sched_date} {self.sched_time}"