from blog.models import Page
from website.models import Contact, Service, Testimonial


class CustomMiddleWares(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.contact = Contact.objects.first()
        request.pages = Page.objects.filter(visible=True).order_by("title")[:5]
        request.services = Service.objects.filter(visible=True)
        request.testimonials = Testimonial.objects.filter(visible=True)
        return self.get_response(request)
