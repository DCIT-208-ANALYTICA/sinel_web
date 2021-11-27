from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from accounts.models import Administrator


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
            messages.add_message(request, messages.ERROR, "Invalid credentials")
            return render(request, self.template_name)
        

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("website:index")

class ChangePasswordView(View):
    def post(self, request, *args, **kwargs):
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        current_password = request.POST.get("current_password")
        admin_id = request.POST.get("admin_id")

        user_to_change = get_object_or_404(Administrator, id=admin_id)
        loggedin_user = authenticate(email_address=request.user.email_address, password=current_password)

        if not loggedin_user:
            messages.add_message(request, messages.ERROR, "Invalid credentials")
        elif password != repeat_password:
            messages.add_message(request, messages.ERROR, "Passwords do not match.")
        elif loggedin_user.is_superuser or loggedin_user == user_to_change:
            user_to_change.set_password(password)
            user_to_change.save()
            messages.add_message(request, messages.SUCCESS, "Password updated successfully.")
        elif loggedin_user == user_to_change:
            login(request, loggedin_user)
        else:
            messages.add_message(request, messages.ERROR, "Forbidden")
        return redirect(request.META.get("HTTP_REFERER"))