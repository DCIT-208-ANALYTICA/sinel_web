from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_api_v1.utils import ResponseMessage
from website.forms import ContactForm
from website.models import Contact
from .serializers import ContactSerializer
from django.utils.html import strip_tags


class ContactApi(generics.GenericAPIView):
    """
    Returns the contact details.
    """
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer
    form_class = ContactForm

    def get(self, request, **kwargs):
        contact = Contact.objects.first()
        data = self.serializer_class(contact).data
        return Response({"contact": data})

    def put(self, request, **kwargs):
        contact = Contact.objects.first()
        form = self.form_class(request.data, instance=contact)
        if form.is_valid():
            form.save()
            data = self.serializer_class(contact).data
            return Response({"contact": data})
        else:
            # Return the first error.
            for field, er in form.errors.items():
                message = f"{field}: [{strip_tags(er)}]"
                response = ResponseMessage(ResponseMessage.ERROR, message)
                return Response({"response": response.to_json()})
