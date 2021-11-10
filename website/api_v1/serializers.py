from rest_framework import serializers
from website.models import Contact, Gallery, Service


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
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
