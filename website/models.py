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

#Social_Media_Link
class Social_Media_Link(model.Models):
    Name=models.CharField(max_length=100)
    Icon_Url=models.URLField(max_length=200)
    Link=models.CharField(max_length=100)

# Insurance Partner
class Insurance_Partner(model.Models):
    Name=models.CharField(max_length=100)
    Description=models.CharField(max_length=200)
    LOGO=models.URLField(max_length=200)
    Visible=models.BooleanField(default=False)

# Gallery
class Gallery(model.Models):
    Title=models.CharField(max_length=100)
    Description=models.CharField(max_length=200)
    Type=models.CharField(max_length=200)
    URL=models.URLField(max_length=200)
    Visible=models.BooleanField(default=False)

# Healt-Tips
class Health_Tips(model.Models):
    Title=models.CharField(max_length=100)
    Slug=models.CharField(max_length=100)
    Content=models.CharField(max_length=200)

# Banner
class Banner(model.Models):
    Title=models.CharField(max_length=100)
    Description=models.CharField(max_length=200,null=True)
    Type=models.CharField(max_length=200)
    URL=models.URLField(max_length=200,null=True)
    Image=models.ImageField(max_length=200)
    Visible=models.BooleanField(default=False)

# Services
class Services(model.Models):
    Title=models.CharField(max_length=100)
    Description=models.CharField(max_length=200,null=True)
    Image=models.ImageField(max_length=200)
    Visible=models.BooleanField(default=False)

# client
class Client(model.Models):
    Story=models.CharField(max_length=500)
    Description=models.CharField(max_length=200)
    Image=models.ImageField(max_length=200)
    Visible=models.BooleanField(default=False)

# Open hour
class Client(model.Models):
    DAYS=models.CharField(max_length=500)
    tIME=models.CharField(max_length=200)
    




   
   
    

    

    