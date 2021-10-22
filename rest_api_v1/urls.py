from django.urls import path
from website.api_v1 import views as website_api
from accounts.api_v1 import views as account_api

urlpatterns = [
    path("contact", website_api.ContactApi.as_view()),
    path("administrators", account_api.AdministratorsApi.as_view()),
    path("administrators/<str:email_address>", account_api.AdministratorApi.as_view()),
    path("administrators/register/", account_api.RegisterAdministrator.as_view()),
    path("administrators/login/", account_api.LoginAdministratorApi.as_view()),
    path("administrators/change_password/", account_api.ChangeAdministratorPasswordApi.as_view()),
]