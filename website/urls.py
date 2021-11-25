from django.urls import path
from . import views


app_name = "website"


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about", views.AboutView.as_view(), name="about"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path("gallery", views.GalleryView.as_view(), name="gallery"),
    path("services", views.ServicesView.as_view(), name="services"),
    path("details", views.DetailsView.as_view(), name="details")
]
