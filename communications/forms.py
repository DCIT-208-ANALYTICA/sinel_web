from django.db.models import fields
from django.forms import ModelForm
from .models import Appointment

# Creating form class


class AppointmnentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
