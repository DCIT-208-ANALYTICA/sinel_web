from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from .managers import AdministratorManager


class Administrator(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    email_address = models.EmailField(unique=True)
    photo = models.ImageField(upload_to="uploads/users", blank=True, null=True)
    last_login_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    username = None
    USERNAME_FIELD = "email_address"
    objects = AdministratorManager()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.fullname or self.email_address
