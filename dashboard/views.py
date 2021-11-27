from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.utils.decorators import method_decorator
from communications.models import Appointment
from sinel_web.utils.decorators import staff_only
from website.models import About, Album,Contact, Media, Service
from accounts.models import Administrator
from django.contrib import messages


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


class AdministratorsView(View):
    template_name = "dashboard/administrators.html"

    @method_decorator(staff_only())
    def get(self, request, *args, **kwargs):
        context = {"administrators": Administrator.objects.all()}
        return render(request, self.template_name, context)


class AdministratorDetailsView(View):
    template_name = "dashboard/administrator_details.html"

    @method_decorator(staff_only())
    def get(self, request, admin_id, *args, **kwargs):
        context = {
            "administrator": get_object_or_404(Administrator, id=admin_id)
        }
        return render(request, self.template_name, context)

    def post(self, request, admin_id, *args, **kwargs):
        admin = get_object_or_404(Administrator, id=admin_id)
        photo = request.FILES.get("photo")
        fullname = request.POST.get("fullname")
        title = request.POST.get("title")
        is_active = request.POST.get("is_active", "")

        if photo:
            admin.photo = photo
        admin.fullname = fullname
        admin.title = title
        admin.is_active = "on" in is_active
        admin.save()
        return redirect(request.META.get("HTTP_REFERER"))


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
        context = {"albumns": Album.objects.all()}
        return render(request, self.template_name, context)


class AlbumView(View):
    template_name = "dashboard/album_items.html"

    @method_decorator(staff_only())
    def get(self, request, album_id, *argd, **kwargs):
        album = get_object_or_404(Album, id=album_id)
        context = {"album": album}
        return render(request, self.template_name, context)


class CreateUpdateAlbum(View):
    template_name = "dashboard/create_update_album.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        album_id = request.GET.get("album_id", -1)
        context = {"album": Album.objects.filter(id=album_id).first()}
        return render(request, self.template_name, context)

    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        album_id = request.POST.get("album_id") or None
        name = request.POST.get("name")
        service = Album.objects.filter(id=album_id).first()
        if service:
            # Update
            service.name = name
            service.save()
        else:
            Album.objects.create(name=name)
        return redirect("dashboard:gallery")


class CreateUpdateMedia(View):
    template_name = "dashboard/create_update_media.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        media_id = request.GET.get("media_id", -1) or None
        context = {
            "albums": Album.objects.all(),
            "media": Media.objects.filter(id=media_id).first(),
        }
        return render(request, self.template_name, context)

    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        media_id = request.POST.get("media_id") or None
        name = request.POST.get("name")
        description = request.POST.get("description")
        visible = "on" in request.POST.get("visible", "")
        file = request.FILES.get("file")

        album = get_object_or_404(Album, id=request.POST.get("album"))

        media = Media.objects.filter(id=media_id).first()
        if media:
            # Update
            media.name = name
            media.description = description
            media.visible = visible
            media.album = album
            if file:
                media.file = file
            media.save()
        else:
            Media.objects.create(name=name,
                                 description=description,
                                 visible=visible,
                                 album=album,
                                 file=file)
        return redirect("dashboard:album", album_id=media.album.id)


class ServicesView(View):
    template_name = "dashboard/services.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        context = {"services": Service.objects.all()}
        return render(request, self.template_name, context)


class CreateUpdateService(View):
    template_name = "dashboard/create_update_service.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        service_id = request.GET.get("service_id", -1)
        context = {"service": Service.objects.filter(id=service_id).first()}
        return render(request, self.template_name, context)

    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        service_id = request.POST.get("service_id") or None
        title = request.POST.get("title")
        description = request.POST.get("service_description")
        visible = "on" in request.POST.get("visible", "")
        image = request.FILES.get("image")

        service = Service.objects.filter(id=service_id).first()
        if service:
            # Update
            service.title = title
            service.description = description
            service.visible = visible
            if image:
                service.image = image
            service.save()
        else:
            Service.objects.create(title=title,
                                   description=description,
                                   visible=visible,
                                   image=image)
            messages.add_message(request, messages.SUCCESS,
                                 "New service created successfully.")
        return redirect("dashboard:services")


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


class AppointmentView(View):
    template_name = "dashboard/appointments.html"

    def get(self, request, *argd, **kwargs):
        context = {"appointments": Appointment.objects.filter()}

        return render(request, self.template_name, context)
