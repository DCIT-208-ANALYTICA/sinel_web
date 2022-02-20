from django.db import models


# Create your models here.
class Appointment(models.Model):
    fullname = models.CharField(max_length=70)
    email = models.EmailField(max_length=254, blank=True, null=True)
    number = models.CharField(max_length=13)  #Incase of +233
    date = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField(null=True, blank=True)
    message = models.TextField()
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.fullname