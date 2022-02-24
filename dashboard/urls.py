from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about", views.AboutView.as_view(), name="about"),
    path("appointments", views.AppointmentView.as_view(), name="appointments"),
    path("gallery", views.GalleryView.as_view(), name="gallery"),
    path("album/<str:album_id>", views.AlbumView.as_view(), name="album"),
    path(
        "create_update_album",
        views.CreateUpdateAlbum.as_view(),
        name="create_update_album",
    ),
    path("delete_album", views.DeleteAlbumView.as_view(), name="delete_album"),
    path(
        "create_update_media",
        views.CreateUpdateMedia.as_view(),
        name="create_update_media",
    ),
    path("delete_media", views.DeleteMediaView.as_view(), name="delete_media"),
    path("services", views.ServicesView.as_view(), name="services"),
    path(
        "create_update_service",
        views.CreateUpdateService.as_view(),
        name="create_update_service",
    ),
    path("delete_service",
         views.DeleteServiceView.as_view(),
         name="delete_service"),
    path("team_leads", views.TeamLeadsView.as_view(), name="team_leads"),
    path(
        "create_update_team_lead",
        views.CreateUpdateTeamLead.as_view(),
        name="create_update_team_lead",
    ),
    path("delete_team_lead",
         views.DeleteTeamLeadView.as_view(),
         name="delete_team_lead"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path("clients", views.ClientsView.as_view(), name="clients"),
    path("posts", views.PostsView.as_view(), name="posts"),
    path("banners", views.BannersView.as_view(), name="banners"),
    path("create_update_post",
         views.CreateUpdatePostView.as_view(),
         name="create_update_post"),
    path("delete_post", views.DeletePostView.as_view(), name="delete_post"),

    # Testimonials
    path("testimonials", views.TestimonialsView.as_view(),
         name="testimonials"),
    path(
        "create_update_testimonial",
        views.CreateUpdateTestimonial.as_view(),
        name="create_update_testimonial",
    ),
    path("delete_testimonial",
         views.DeleteTestimonialView.as_view(),
         name="delete_testimonial"),

    # Partners
    path("partners", views.PartnersView.as_view(), name="partners"),
    path(
        "create_update_partner",
        views.CreateUpdatePartner.as_view(),
        name="create_update_partner",
    ),
    path("delete_partner",
         views.DeletePartnerView.as_view(),
         name="delete_partner"),

    # Pages
    path("pages", views.PagesView.as_view(), name="pages"),
    path(
        "create_update_page",
        views.CreateUpdatePageView.as_view(),
        name="create_update_page",
    ),
    path("delete_page", views.DeletePageView.as_view(), name="delete_page"),

    # Notifications
    path("notifications",
         views.NotificationsView.as_view(),
         name="notifications"),
    path(
        "create_update_notification",
        views.CreateUpdateNotificationView.as_view(),
        name="create_update_notification",
    ),
    path("delete_notification",
         views.DeleteNotificationView.as_view(),
         name="delete_notification"),
]
