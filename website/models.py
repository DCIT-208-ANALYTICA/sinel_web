from django.db import models
from django.db.models.base import Model

# Create your models here.

DAYS_OF_WEEK = (
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
    (6, "Sunday"),
)
#


class ContactDataEntity(model.Models):
    gps = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    long = models.FloatField()
    lat = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SocialMediaLink(model.Models):
    name = models.CharField(max_length=100)
    icon_url = models.URLField(max_length=200)
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Insurance Partner
class InsurancePartner(model.Models):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    logo = models.URLField(max_length=200)
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Gallery
class Gallery(model.Models):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Healt-Tips
class HealthTips(model.Models):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Banner(model.Models):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    url = models.URLField(max_length=200, null=True)
    image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100
    )
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Services(Model.Models):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100
    )
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Client(model.Models):
    title = models.CharField(max_length=30)
    story = models.TextField()
    image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100
    )
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Open hour
class OpeningHour(model.Models):
    days = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    time = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Team_lead
class TeamLead(model.Models):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100
    )
    Visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# About
class About(model.Models):
    overview = models.CharField(max_length=200)
    mission = models.CharField(max_length=500)
    vision = models.CharField(max_length=500)
    value = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
