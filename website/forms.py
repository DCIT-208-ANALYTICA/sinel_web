from django import forms
from .models import About, Client, Contact, Gallery, Service, TeamLead


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = [
            "id",
            "created_at",
            "update_at",
        ]


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        exclude = [
            "id",
            "created_at",
            "update_at",
        ]


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        exclude = [
            "id",
            "created_at",
            "update_at",
        ]


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = [
            "id",
            "created_at",
            "update_at",
        ]


class TeamLeadForm(forms.ModelForm):
    class Meta:
        model = TeamLead
        exclude = [
            "id",
            "created_at",
            "update_at",
        ]


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = [
            "id",
            "created_at",
            "update_at",
        ]
