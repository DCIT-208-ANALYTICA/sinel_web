from django import forms
from .models import Contact, Gallery


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
