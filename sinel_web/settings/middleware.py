from website.models import Contact


class CustomMiddleWares(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.contact = Contact.objects.first()
        return self.get_response(request)
