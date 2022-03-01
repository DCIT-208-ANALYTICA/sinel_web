from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from .models import About, Media, Partner, Service, TeamLead, Testimonial
from blog.models import Page, Post


class IndexView(View):
    template_name = "website/index.html"

    def get(self, request, *args, **kwargs):
        context = {
            "about": About.objects.first(),
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
    template_name = "website/team.html"

    def get(self, request, *args, **kwargs):
        team_leads = TeamLead.objects.filter(visible=True)
        specialities = team_leads.values("title").distinct()
        specialities = set([item["title"] for item in specialities])
        context = {
            "doctors": team_leads,
            "specialities": specialities,
        }
        return render(request, self.template_name, context)


class OurPatnersView(View):
    template_name = "website/our_partners.html"

    def get(self, request, *args, **kwargs):
        partners = Partner.objects.filter(visible=True).order_by("category")
        categories = partners.values("category").distinct()
        categories = set([cat["category"] for cat in categories])
        context = {
            "categories": categories,
            "partners": partners,
        }
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


class StaticPageView(View):
    template_name = "website/static_page.html"

    def get(self, request, page_id, *args, **kwargs):
        page = get_object_or_404(Page, id=page_id)
        context = {
            "page": page,
        }
        return render(request, self.template_name, context)
