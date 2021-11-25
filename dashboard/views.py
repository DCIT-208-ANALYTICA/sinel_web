from django.shortcuts import render
from django.views.generic import View


class Index(View):
    template_name = "dashboard/index.html"

    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, self.template_name, context)