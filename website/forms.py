from django import forms
from .models import Contact, Gallery, Service


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
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
