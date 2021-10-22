from django.urls import path
from website.api_v1 import views as website_api
from accounts.api_v1 import views as account_api

urlpatterns = [
    path("contact", website_api.ContactApi.as_view()),
    path("accounts/administrators", account_api.AdministratorsApi.as_view()),
    path("accounts/administrators/<int:admin_id>", account_api.AdministratorApi.as_view()),
    path("accounts/register/", account_api.RegisterAdministrator.as_view()),
    path("accounts/login/", account_api.LoginAdministratorApi.as_view()),
]