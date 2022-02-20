from django.db import models
from accounts.models import Administrator
from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field()
    thumbnail = models.ImageField(upload_to="uploads/images")
    tags = models.CharField(max_length=200)
    by = models.ForeignKey(Administrator, on_delete=models.PROTECT)
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    content = CKEditor5Field()
    by = models.ForeignKey(Administrator, on_delete=models.PROTECT)
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = "-".join(self.title.lower().split())
        return super().save(*args, **kwargs)