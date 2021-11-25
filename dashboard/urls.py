from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("about", views.About.as_view(), name="about"),
    path("gallery", views.Gallery.as_view(), name="gallery"),
    path("services", views.Services.as_view(), name="services"),
    path("teamleads", views.TeamLeads.as_view(), name="teamleads"),
    path("contact", views.Contact.as_view(), name="contact"),
    path("clients", views.Clients.as_view(), name="clients"),
    path("blog", views.Blog.as_view(), name="blog"),
    path("banners", views.Banners.as_view(), name="banners"),
]
