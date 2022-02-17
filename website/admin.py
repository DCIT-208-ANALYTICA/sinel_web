from django.contrib import admin
from .models import *

admin.site.register(Contact)
admin.site.register(SocialMediaLink)
admin.site.register(InsurancePartner)
admin.site.register(HealthTips)
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(OpeningHour)
admin.site.register(TeamLead)
admin.site.register(About)
admin.site.register(Media)

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
