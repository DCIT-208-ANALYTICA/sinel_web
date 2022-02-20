from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from .models import About, Media, Service, TeamLead, Testimonial
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


class DoctorsView(View):
    template_name = "website/doctors.html"

    def get(self, request, *args, **kwargs):
        context = {"doctors": TeamLead.objects.filter(visible=True)}
        return render(request, self.template_name, context)


class OurPatnersView(View):
    template_name = "website/our_partners.html"

    def get(self, request, *args, **kwargs):
        context = {"services": Service.objects.filter(visible=True)}
        return render(request, self.template_name, context)


class ServiceDetailsView(View):
    template_name = "website/service_details.html"

    def get(self, request, service_id, *args, **kwargs):
        service = get_object_or_404(Service, id=service_id)
        doctors = service.doctors.filter(visible=True)
        testimonials = service.testimonials.filter(visible=True)
        context = {
            "service": service,
            "doctors": doctors,
            "testimonials": testimonials,
        }
        return render(request, self.template_name, context)
