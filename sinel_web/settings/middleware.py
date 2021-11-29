from website.models import Contact, Service


class CustomMiddleWares(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.contact = Contact.objects.first()
        request.services = Service.objects.filter(visible=True)
        return self.get_response(request)
