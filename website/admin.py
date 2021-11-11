from django.contrib import admin
from .models import Contact

# Create only one contact model that can be updated.
try:
    contact = Contact.objects.first()
    if not contact:
        Contact.objects.create(gps="None",
                               email="info@sinelhospital.com",
                               address="Accra",
                               telephone="020000000",
                               lat_lng="0.03,30.93")
except Exception as e:
    print(e)