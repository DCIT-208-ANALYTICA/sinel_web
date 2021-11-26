from django.shortcuts import render
from django.views.generic import View
from .models import Service


class IndexView(View):
    template_name = "website/index.html"

    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class AboutView(View):
    template_name = "website/about.html"

    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class ContactView(View):
    template_name = "website/contact.html"

    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class GalleryView(View):
    template_name = "website/gallery.html"

    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class ServicesView(View):
    template_name = "website/services.html"

    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class ServiceDetailsView(View):
    template_name = "website/service_details.html"

    def get(self, request, *args, **kwargs):
        context = {
            "service": Service.objects.filter().last()
        }

        return render(request, self.template_name, context)
