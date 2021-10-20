from django.urls import path
from website.api_v1 import views as website_api

urlpatterns = [
    path("contact", website_api.ContactApi.as_view()),
]