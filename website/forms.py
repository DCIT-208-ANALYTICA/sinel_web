from django import forms
from .models import (About, Client, Contact, Media, OpeningHour, Service,
                     SocialMediaLink, TeamLead, Testimonial)


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


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        exclude = [
            "id",
            "media_type",
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


class OpeningHourForm(forms.ModelForm):
    class Meta:
        model = OpeningHour
        exclude = [
            "id",
            "created_at",
            "update_at",
        ]


class SocialMediaLinkForm(forms.ModelForm):
    class Meta:
        model = SocialMediaLink
        exclude = [
            "id",
            "created_at",
            "update_at",
        ]


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        exclude = [
            "id",
            "added_by",
            "created_at",
            "update_at",
        ]