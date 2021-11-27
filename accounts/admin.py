from django.contrib import admin
from . models import Administrator

# Register your models here.
admin.site.register(Administrator)

# Create default superuser
try:
    superadmin, created = Administrator.objects.get_or_create(email_address="admin@email.com", is_superuser=True)
    print("created", created)
    if created or True:
        superadmin.set_password("admin")
        superadmin.save()
        print("Super user created")
except Exception as e:
    print("Failed to create defautl superuser.: " + str(e))
