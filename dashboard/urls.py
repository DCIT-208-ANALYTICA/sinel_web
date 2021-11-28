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
    path(
        "create_update_media",
        views.CreateUpdateMedia.as_view(),
        name="create_update_media",
    ),
    path("services", views.ServicesView.as_view(), name="services"),
    path(
        "create_update_service",
        views.CreateUpdateService.as_view(),
        name="create_update_service",
    ),
    path("delete_service", views.DeleteServiceView.as_view(), name="delete_service"),
    path("teamleads", views.TeamLeadsView.as_view(), name="teamleads"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path("clients", views.ClientsView.as_view(), name="clients"),
    path("blog", views.BlogView.as_view(), name="blog"),
    path("banners", views.BannersView.as_view(), name="banners"),
    path("update_blog", views.UpdateBlogPost.as_view(), name="update_blog"),
]
