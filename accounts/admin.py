from django.contrib import admin
from . models import Administrator

# Register your models here.
admin.site.register(Administrator)

# Create default superuser
try:
    superadmin, created = Administrator.objects.get_or_create(email_address="admin@email.com", is_superuser=True, is_staff=True)
    print("Created: ", created)
    if created:
        superadmin.set_password("admin")
        superadmin.save()
        print("Set default password.")
except Exception as e:
    print("Failed to create defautl superuser.: " + str(e))
