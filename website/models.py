from django.db import models

# Create your models here.

class AdminData(model.Models):
    Username=models.CharField(max_length=100)
    Email_Adress=models.EmailField()
    Fullname=models.CharField(max_length=100)
    Is_Super_User=models.BooleanField(default=False)

    