from django.db import models

# Create your models here.
class user_pat(models.Model):
    user_username = models.CharField(max_length=254)
    user_password = models.CharField(max_length=254)
    user_email = models.EmailField(max_length=254)

class SpecializationListModel(models.Model):
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.specialty