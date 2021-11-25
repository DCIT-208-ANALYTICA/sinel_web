from django.shortcuts import render
from django.views.generic import View


class Index(View):
    template_name = "dashboard/index.html"

    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class About(View):
    template_name = "dashboard/about.html"

    def get(self, request, *argd, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class Contact(View):
    template_name = "dashboard/contact.html"

    def get(self, request, *argd, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class Gallery(View):
    template_name = "dashboard/gallery.html"

    def get(self, request, *argd, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class Services(View):
    template_name = "dashboard/services.html"

    def get(self, request, *argd, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class TeamLeads(View):
    template_name = "dashboard/teamleads.html"

    def get(self, request, *argd, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class Banners(View):
    template_name = "dashboard/banners.html"

    def get(self, request, *argd, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class Clients(View):
    template_name = "dashboard/clients.html"

    def get(self, request, *argd, **kwargs):
        context = {}

        return render(request, self.template_name, context)


class Blog(View):
    template_name = "dashboard/blog.html"

    def get(self, request, *argd, **kwargs):
        context = {}

        return render(request, self.template_name, context)
