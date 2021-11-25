from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about", views.AboutView.as_view(), name="about"),
    path("administrators", views.AdministratorsView.as_view(), name="administrators"),
    path("gallery", views.GalleryView.as_view(), name="gallery"),
    path("services", views.ServicesView.as_view(), name="services"),
    path("teamleads", views.TeamLeadsView.as_view(), name="teamleads"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path("clients", views.ClientsView.as_view(), name="clients"),
    path("blog", views.BlogView.as_view(), name="blog"),
    path("banners", views.BannersView.as_view(), name="banners"),
]
