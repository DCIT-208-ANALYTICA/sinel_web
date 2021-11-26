from django.shortcuts import redirect, render
from .forms import AppointmnentForm
from django.views.generic import View

# Create your views here.
class BookAppointment(View):
    template_name = ""
    form_class = AppointmnentForm

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect(request.META.get("HTTP_REFERER"))
