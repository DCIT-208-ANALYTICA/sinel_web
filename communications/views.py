from django.shortcuts import render
from .forms import AppointmnentForm
from django.views.generic import View

# Create your views here.
class BookAppointment(View):
    template_name = ""
    form_class = AppointmnentForm

    def get(self, request, **kwargs):
        pass

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            appointment = form.save()
