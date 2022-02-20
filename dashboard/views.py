from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.utils.decorators import method_decorator
from blog.forms import PostForm
from communications.models import Appointment
from sinel_web.utils.decorators import staff_only
from website.models import About, Album, Contact, Media, Partner, Service, TeamLead, Testimonial
from blog.models import Post
from django.contrib import messages
from website.forms import MediaForm, ServiceForm, TeamLeadForm, TestimonialForm, PartnerForm
from django.utils.html import strip_tags
from accounts.models import Administrator


class IndexView(View):
    template_name = "dashboard/index.html"

    @method_decorator(staff_only())
    def get(self, request, *args, **kwargs):
        context = {
            "posts": Post.objects.all(),
            "administrators": Administrator.objects.all(),
            "services": Service.objects.all(),
            "about": About.objects.first()
        }
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


class ContactView(View):
    template_name = "dashboard/contact.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        context = {"contact": Contact.objects.first()}
        return render(request, self.template_name, context)

    @method_decorator(staff_only())
    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        gps = request.POST.get("gps")
        address = request.POST.get("address")
        telephone = request.POST.get("telephone")
        lat_lng = request.POST.get("lat_lng")

        contact = Contact.objects.first()

        if email:
            contact.email = email
        if gps:
            contact.gps = gps
        if address:
            contact.address = address
        if telephone:
            contact.telephone = telephone
        if lat_lng:
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


class DeleteAlbumView(View):
    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        album_id = request.POST.get("album_id")
        Album.objects.filter(id=album_id).delete()
        return redirect(request.META.get("HTTP_REFERER"))


class CreateUpdateMedia(View):
    template_name = "dashboard/create_update_media.html"
    form_class = MediaForm
    model_class = Media
    object_id_field = "media_id"

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
        object_id = request.POST.get(self.object_id_field) or None
        instance = None
        if object_id:
            instance = get_object_or_404(self.model_class, id=object_id)
        form = self.form_class(request.POST,
                               request.FILES or None,
                               instance=instance)
        if form.is_valid():
            media = form.save()
        else:
            for field, er in form.errors.items():
                message = f"{field.title()}: {strip_tags(er)}"
                messages.add_message(request, messages.ERROR, message)
            return redirect(request.META.get("HTTP_REFERER"))
        return redirect(to="dashboard:album", album_id=media.album.id)


class DeleteMediaView(View):
    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        media_id = request.POST.get("media_id")
        Media.objects.filter(id=media_id).delete()
        return redirect(request.META.get("HTTP_REFERER"))


class ServicesView(View):
    template_name = "dashboard/services.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        context = {"services": Service.objects.all()}
        return render(request, self.template_name, context)


class CreateUpdateService(View):
    template_name = "dashboard/create_update_service.html"
    form_class = ServiceForm
    model_class = Service
    object_id_field = "service_id"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        service_id = request.GET.get("service_id", -1)
        context = {
            "service": Service.objects.filter(id=service_id).first(),
            "doctors": TeamLead.objects.filter(visible=True),
        }
        return render(request, self.template_name, context)

    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        object_id = request.POST.get(self.object_id_field) or None
        instance = None
        if object_id:
            instance = get_object_or_404(self.model_class, id=object_id)
        form = self.form_class(request.POST,
                               request.FILES or None,
                               instance=instance)
        if form.is_valid():
            form.save()
        else:
            for field, er in form.errors.items():
                message = f"{field.title()}: {strip_tags(er)}"
                messages.add_message(request, messages.ERROR, message)
            return redirect(request.META.get("HTTP_REFERER"))
        return redirect("dashboard:services")


class DeleteServiceView(View):
    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        service_id = request.POST.get("service_id")
        Service.objects.filter(id=service_id).delete()
        return redirect(request.META.get("HTTP_REFERER"))


class TeamLeadsView(View):
    template_name = "dashboard/team_leads.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        context = {"team_leads": TeamLead.objects.all().order_by("-id")}
        return render(request, self.template_name, context)


class CreateUpdateTeamLead(View):
    template_name = "dashboard/create_update_team_lead.html"
    form_class = TeamLeadForm
    model_class = TeamLead
    object_id_field = "team_lead_id"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        team_lead_id = request.GET.get("team_lead_id", -1)
        context = {
            "team_lead": TeamLead.objects.filter(id=team_lead_id).first()
        }
        return render(request, self.template_name, context)

    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        object_id = request.POST.get(self.object_id_field) or None
        instance = None
        if object_id:
            instance = get_object_or_404(self.model_class, id=object_id)
        form = self.form_class(request.POST,
                               request.FILES or None,
                               instance=instance)
        if form.is_valid():
            form.save()
        else:
            for field, er in form.errors.items():
                message = f"{field.title()}: {strip_tags(er)}"
                messages.add_message(request, messages.ERROR, message)
            return redirect(request.META.get("HTTP_REFERER"))
        return redirect("dashboard:team_leads")


class DeleteTeamLeadView(View):
    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        team_lead_id = request.POST.get("team_lead_id")
        TeamLead.objects.filter(id=team_lead_id).delete()
        return redirect(request.META.get("HTTP_REFERER"))


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


class PostsView(View):
    template_name = "dashboard/posts.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        context = {"posts": Post.objects.all()}
        return render(request, self.template_name, context)


class CreateUpdatePostView(View):
    template_name = "dashboard/create_update_post.html"
    form_class = PostForm
    model_class = Post
    object_id_field = "blog_id"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        post_id = request.GET.get("post_id", -1)
        context = {"post": self.model_class.objects.filter(id=post_id).first()}
        return render(request, self.template_name, context)

    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        object_id = request.POST.get(self.object_id_field) or None
        instance = None
        if object_id:
            instance = get_object_or_404(self.model_class, id=object_id)
        form = self.form_class(request.POST,
                               request.FILES or None,
                               instance=instance)
        if form.is_valid():
            post = form.save(commit=False)
            post.by = request.user
            post.save()
        else:
            for field, er in form.errors.items():
                message = f"{field.title()}: {strip_tags(er)}"
                messages.add_message(request, messages.ERROR, message)
            return redirect(request.META.get("HTTP_REFERER"))
        return redirect("dashboard:posts")


class DeletePostView(View):
    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        post_id = request.POST.get("post_id")
        Post.objects.filter(id=post_id).delete()
        return redirect(request.META.get("HTTP_REFERER"))


class AppointmentView(View):
    template_name = "dashboard/appointments.html"

    def get(self, request, *argd, **kwargs):
        context = {
            "appointments": Appointment.objects.filter().order_by("-id")
        }

        return render(request, self.template_name, context)


class TestimonialsView(View):
    template_name = "dashboard/testimonials.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        testimonials = Testimonial.objects.all()
        context = {"testimonials": testimonials}
        return render(request, self.template_name, context)


class CreateUpdateTestimonial(View):
    template_name = "dashboard/create_update_testimonial.html"
    form_class = TestimonialForm
    model_class = Testimonial
    object_id_field = "testimonial_id"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        testimonial_id = request.GET.get("testimonial_id", -1)
        context = {
            "services": Service.objects.filter(visible=True),
            "doctors": TeamLead.objects.filter(visible=True),
            "testimonial":
            Testimonial.objects.filter(id=testimonial_id).first()
        }
        return render(request, self.template_name, context)

    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        object_id = request.POST.get(self.object_id_field) or None
        instance = None
        if object_id:
            instance = get_object_or_404(self.model_class, id=object_id)
        form = self.form_class(request.POST,
                               request.FILES or None,
                               instance=instance)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.added_by = request.user
            testimonial.save()
        else:
            for field, er in form.errors.items():
                message = f"{field.title()}: {strip_tags(er)}"
                messages.add_message(request, messages.ERROR, message)
            return redirect(request.META.get("HTTP_REFERER"))
        return redirect("dashboard:testimonials")


class DeleteTestimonialView(View):
    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        testimonial_id = request.POST.get("testimonial_id")
        Testimonial.objects.filter(id=testimonial_id).delete()
        return redirect(request.META.get("HTTP_REFERER"))


class PartnersView(View):
    template_name = "dashboard/partners.html"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        context = {"partners": Partner.objects.all().order_by("-id")}
        return render(request, self.template_name, context)


class CreateUpdatePartner(View):
    template_name = "dashboard/create_update_partner.html"
    form_class = PartnerForm
    model_class = Partner
    object_id_field = "partner_id"

    @method_decorator(staff_only())
    def get(self, request, *argd, **kwargs):
        partner_id = request.GET.get("partner_id", -1)
        context = {"partner": Partner.objects.filter(id=partner_id).first()}
        return render(request, self.template_name, context)

    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        object_id = request.POST.get(self.object_id_field) or None
        instance = None
        if object_id:
            instance = get_object_or_404(self.model_class, id=object_id)
        form = self.form_class(request.POST,
                               request.FILES or None,
                               instance=instance)
        if form.is_valid():
            form.save()
        else:
            for field, er in form.errors.items():
                message = f"{field.title()}: {strip_tags(er)}"
                messages.add_message(request, messages.ERROR, message)
            return redirect(request.META.get("HTTP_REFERER"))
        return redirect("dashboard:partners")


class DeletePartnerView(View):
    @method_decorator(staff_only())
    def post(self, request, *argd, **kwargs):
        partner_id = request.POST.get("partner_id")
        Partner.objects.filter(id=partner_id).delete()
        return redirect(request.META.get("HTTP_REFERER"))
