from rest_framework import serializers
from website.models import About, Client, Contact, Gallery, Service, TeamLead


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ["created_at", "updated_at"]


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        exclude = ["created_at", "updated_at"]


class GallerySerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    def get_file(self, item):
        request = self.context.get("request")
        if item.file:
            url = item.file.url
            return request.build_absolute_uri(url)
        return ""

    class Meta:
        model = Gallery
        exclude = ["created_at", "updated_at"]


class ServiceSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, item):
        request = self.context.get("request")
        if item.image:
            url = item.image.url
            return request.build_absolute_uri(url)
        return ""

    class Meta:
        model = Service
        exclude = ["created_at", "updated_at"]


class TeamLeadSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, item):
        request = self.context.get("request")
        if item.image:
            url = item.image.url
            return request.build_absolute_uri(url)
        return ""

    class Meta:
        model = TeamLead
        exclude = ["created_at", "updated_at"]


class ClientSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, item):
        request = self.context.get("request")
        if item.image:
            url = item.image.url
            return request.build_absolute_uri(url)
        return ""

    class Meta:
        model = Client
        exclude = ["created_at", "updated_at"]
