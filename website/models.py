from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

DAYS_OF_WEEK = (
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
    (6, "Sunday"),
)


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
    image = models.ImageField(upload_to="uploads/images")
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
    description = models.TextField()
    file_type = models.CharField(max_length=20)
    file = models.FileField(max_length=200)
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
    image = models.ImageField(upload_to="uploads/images")
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="uploads/images", )
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Client(models.Model):
    title = models.CharField(max_length=30)
    story = models.TextField()
    image = models.ImageField(upload_to="uploads/images", )
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OpeningHour(models.Model):
    days = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    time = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TeamLead(models.Model):
    fullname = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    image = models.ImageField(upload_to="uploads/images", )
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class About(models.Model):
    overview = CKEditor5Field()
    mission = CKEditor5Field()
    vision = CKEditor5Field()
    value = CKEditor5Field()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
