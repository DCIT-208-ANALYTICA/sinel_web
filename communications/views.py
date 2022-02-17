from django.shortcuts import redirect, render
from .forms import AppointmnentForm
from django.views.generic import View


# Create your views here.
class BookAppointment(View):
    template_name = "communications/appointments.html"
    form_class = AppointmnentForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("website:index")
        else:
            print(form.errors)
        return redirect(request.META.get("HTTP_REFERER"))
