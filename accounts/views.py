from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone


class Login(View):
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
            user.last_login_date = timezone.now()
            user.save()
            redirect_url = request.GET.get("next") or "dashboard:index"
            return redirect(redirect_url)
        else:
            messages.add_message(request, messages.ERROR, "Invalid credentials")
            return render(request, self.template_name)
        
