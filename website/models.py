from django.db import models

# Create your models here.
# Admin Data Entry
class AdminData(model.Models):
    Username=models.CharField(max_length=100)
    Email_Adress=models.EmailField()
    Fullname=models.CharField(max_length=100)
    Is_Super_User=models.BooleanField(default=False)

# Contact_Data_Entity 
class Contact_Data_Entity(model.Models):
    Ghana_Post_Service=models.CharField(max_length=100)
    Email_Adress=models.EmailField()
    Physical_Address=models.CharField(max_length=100)
    Telephone=models.CharField(max_length=100)
    LatLng=models.CharField(max_length=100)
    

    