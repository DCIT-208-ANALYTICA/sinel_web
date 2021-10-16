from django.shortcuts import render


def dashboard(request):
    template_name = "index.html"
    return render(request, template_name)