import os
from django.contrib import admin
from .models import Administrator

# Register your models here.
admin.site.register(Administrator)

SUPER_ADMIN_EMAIL_ADDRESS = os.environ.get("SUPER_ADMIN_EMAIL_ADDRESS",
                                           default="admin@email.com")

SUPER_ADMIN_PASSWORD = os.environ.get("SUPER_ADMIN_PASSWORD", default="admin")

# Create default superuser
try:
    superadmin, created = Administrator.objects.get_or_create(
        email_address=SUPER_ADMIN_EMAIL_ADDRESS,
        is_superuser=True,
        is_staff=True)
    print("Created: ", created)
    if created:
        superadmin.set_password(SUPER_ADMIN_PASSWORD)
        superadmin.save()
        print("Set default password.")
except Exception as e:
    print("Failed to create defautl superuser.: " + str(e))
