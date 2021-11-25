from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from sinel_web.utils.decorators import staff_only


class Index(View):
    template_name = "dashboard/index.html"

    @method_decorator(staff_only("accounts:login"))
    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)