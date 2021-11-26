from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("change_password", views.ChangePasswordView.as_view(), name="change_password"),
    path("logout", views.LogoutView.as_view(), name="logout"),
]
