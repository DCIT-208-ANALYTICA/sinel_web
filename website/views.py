from django.shortcuts import render
from django.views.generic import View
from .models import About, Media, Service, TeamLead
from blog.models import Post


class IndexView(View):
    template_name = "website/index.html"

    def get(self, request, *args, **kwargs):
        context = {
            "team": TeamLead.objects.filter(visible=True),
            "posts": Post.objects.filter(visible=True).order_by("-id")[:5],
        }
        return render(request, self.template_name, context)


class AboutView(View):
    template_name = "website/about.html"

    def get(self, request, *args, **kwargs):
        context = {
            "about": About.objects.first(),
        }
        return render(request, self.template_name, context)


class ContactView(View):
    template_name = "website/contact.html"

    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class GalleryView(View):
    template_name = "website/gallery.html"

    def get(self, request, *args, **kwargs):
        context = {
            "media": Media.objects.filter(visible=True).order_by("-id"),
        }

        return render(request, self.template_name, context)


class ServicesView(View):
    template_name = "website/services.html"

    def get(self, request, *args, **kwargs):
        context = {"services": Service.objects.filter(visible=True)}
        return render(request, self.template_name, context)


class ServiceDetailsView(View):
    template_name = "website/service_details.html"

    def get(self, request, service_id, *args, **kwargs):
        context = {"service": Service.objects.filter(id=service_id).first()}
        return render(request, self.template_name, context)
