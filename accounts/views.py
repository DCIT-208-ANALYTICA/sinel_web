from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from accounts.models import Administrator
from sinel_web.utils.decorators import superuser_only


class LoginView(View):
    template_name = "accounts/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email_address = request.POST.get("email_address")
        password = request.POST.get("password")
        remember_me = True if request.POST.get("remember_me") else False

        user = authenticate(email_address=email_address, password=password)

        if user:
            login(request, user)
            if remember_me:
                request.session.set_expiry(86400 * 30)
            user.last_login_at = timezone.now()
            user.save()
            redirect_url = request.GET.get("next") or "dashboard:index"
            return redirect(redirect_url)
        else:
            messages.add_message(request, messages.ERROR,
                                 "Invalid credentials")
            return render(request, self.template_name)


class AdministratorsView(View):
    template_name = "accounts/administrators.html"

    @method_decorator(superuser_only())
    def get(self, request, *args, **kwargs):
        context = {"administrators": Administrator.objects.all()}
        return render(request, self.template_name, context)


class AdministratorDetailsView(View):
    template_name = "accounts/administrator_details.html"

    @method_decorator(superuser_only())
    def get(self, request, admin_id, *args, **kwargs):
        context = {
            "administrator": get_object_or_404(Administrator, id=admin_id)
        }
        return render(request, self.template_name, context)

    @method_decorator(superuser_only())
    def post(self, request, admin_id, *args, **kwargs):
        admin = get_object_or_404(Administrator, id=admin_id)
        photo = request.FILES.get("photo")
        fullname = request.POST.get("fullname")
        title = request.POST.get("title")
        is_active = request.POST.get("is_active", "")

        if photo:
            admin.photo = photo
        admin.fullname = fullname
        admin.title = title
        admin.is_active = "on" in is_active
        admin.save()
        return redirect(request.META.get("HTTP_REFERER"))


class CreateAdministrator(View):
    template_name = "accounts/create_administrator.html"

    @method_decorator(superuser_only())
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    @method_decorator(superuser_only())
    def post(self, request, *args, **kwargs):
        photo = request.FILES.get("photo")
        fullname = request.POST.get("fullname")
        email_address = request.POST.get("email_address")
        title = request.POST.get("title")
        is_active = "on" in request.POST.get("is_active", "")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")

        if password != repeat_password:
            messages.add_message(request, messages.ERROR,
                                 "Passwords do not match.")
            return redirect("accounts:create_administrator")
        else:
            admin = Administrator.objects.create(
                email_address=email_address,
                fullname=fullname,
                title=title,
                is_active=is_active,
            )
            if photo:
                admin.photo = photo
            admin.set_password(password)
            admin.save()
        return redirect("accounts:administrators")


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("website:index")


class ChangePasswordView(View):
    @method_decorator(superuser_only())
    def post(self, request, *args, **kwargs):
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        current_password = request.POST.get("current_password")
        admin_id = request.POST.get("admin_id")

        user_to_change = get_object_or_404(Administrator, id=admin_id)
        loggedin_user = authenticate(email_address=request.user.email_address,
                                     password=current_password)

        if not loggedin_user:
            messages.add_message(request, messages.ERROR,
                                 "Invalid credentials")
        elif password != repeat_password:
            messages.add_message(request, messages.ERROR,
                                 "Passwords do not match.")
        elif loggedin_user.is_superuser or loggedin_user == user_to_change:
            user_to_change.set_password(password)
            user_to_change.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Password updated successfully.")
        elif loggedin_user == user_to_change:
            login(request, loggedin_user)
        else:
            messages.add_message(request, messages.ERROR, "Forbidden")
        return redirect(request.META.get("HTTP_REFERER"))