from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import View
from django.utils.decorators import method_decorator
from sinel_web.utils.decorators import staff_only
from website.models import About, Contact
from accounts.models import Administrator


class IndexView(View):
    template_name = "dashboard/index.html"

    @method_decorator(staff_only())
    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class AboutView(View):
    template_name = "dashboard/about.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        context = {"about": About.objects.first()}
        return render(request, self.template_name, context)

    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        overview = request.POST.get("overview-content")
        mission = request.POST.get("mission-content")
        vision = request.POST.get("vission-content")
        value = request.POST.get("value-content")

        about = About.objects.first()
        if overview:
            about.overview = overview
        if mission:
            about.mission = mission
        if vision:
            about.vision = vision
        if value:
            about.value = value
        about.save()
        return redirect(request.META.get("HTTP_REFERER"))


class AdministratorInfoView(View):
    template_name = "dashboard/administrators.html"

    @method_decorator(staff_only())
    def get(self, request, *args, **kwargs):
        context = {"administrators": Administrator.objects.all()}
        return render(request, self.template_name, context)


class AdministratorsView(View):
    template_name = "dashboard/administrators.html"

    @method_decorator(staff_only())
    def get(self, request, *args, **kwargs):
        context = {"administrators": Administrator.objects.all()}
        return render(request, self.template_name, context)


class ContactView(View):
    template_name = "dashboard/contact.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        context = {"contact": Contact.objects.first()}
        return render(request, self.template_name, context)

    @method_decorator(staff_only())
    def post(self, request, *args, **kwargs):
        email = request.POST.get("email-content")
        gps = request.POST.get("gps-content")
        address = request.POST.get("address-content")
        telephone = request.POST.get("telephone-content")
        lat_lng = request.POST.get("lat_lng-content")

        contact = Contact.objects.first()

        if email:
            contact.email = email
        if gps:
            contact.gps = gps
        if gps:
            contact.address = address
        if gps:
            contact.telephone = telephone
        if gps:
            contact.lat_lng = lat_lng
        contact.save()
        return redirect(request.META.get("HTTP_REFERER"))


class GalleryView(View):
    template_name = "dashboard/gallery.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class ServicesView(View):
    template_name = "dashboard/services.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class TeamLeadsView(View):
    template_name = "dashboard/teamleads.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class BannersView(View):
    template_name = "dashboard/banners.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class ClientsView(View):
    template_name = "dashboard/clients.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class BlogView(View):
    template_name = "dashboard/blog.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        context = {}

        return render(request, self.template_name, context)
