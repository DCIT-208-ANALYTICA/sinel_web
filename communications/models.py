from django.db import models
from django.db.models.fields import DateField, EmailField

# Create your models here.
class Appointment(models.Model):
    fullname = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    number = models.CharField(max_length=13) #Incase of +233
    date  = models.DateField()
    message = models.TextField()
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
