from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("", views.About.as_view(), name="about"),
    path("", views.Gallery.as_view(), name="gallery"),
    path("", views.Services.as_view(), name="services"),
    path("", views.TeamLeads.as_view(), name="teamleads"),
    path("", views.Contact.as_view(), name="contact"),
    path("", views.Clients.as_view(), name="clients"),
    path("", views.Blog.as_view(), name="blog"),
    path("", views.Banners.as_view(), name="banners"),
]
