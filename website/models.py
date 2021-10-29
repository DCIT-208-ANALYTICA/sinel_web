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


class Contact(models.Model):
    gps = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    lat_lng = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.address


class SocialMediaLink(models.Model):
    name = models.CharField(max_length=100)
    icon_url = models.URLField(max_length=200)
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InsurancePartner(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    logo = models.URLField(max_length=200)
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class HealthTips(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Banner(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    url = models.URLField(max_length=200, null=True)
    image = models.ImageField(upload_to="uploads/banners")
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Services(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(
        upload_to="uploads/services",
        height_field=None,
        width_field=None,
        max_length=100,
    )
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Client(models.Model):
    title = models.CharField(max_length=30)
    story = models.TextField()
    image = models.ImageField(upload_to="uploads/clients",
                              height_field=None,
                              width_field=None,
                              max_length=100)
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OpeningHour(models.Model):
    days = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    time = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TeamLead(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    image = models.ImageField(
        upload_to="uploads/team_leads",
        height_field=None,
        width_field=None,
        max_length=100,
    )
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class About(models.Model):
    overview = models.TextField(max_length=200)
    mission = models.TextField(max_length=500)
    vision = models.TextField(max_length=500)
    value = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
