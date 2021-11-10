from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_api_v1.utils import ResponseMessage
from website.forms import ContactForm, GalleryForm
from website.models import Contact, Gallery
from .serializers import ContactSerializer, GallerySerializer
from django.utils.html import strip_tags


class ContactApi(generics.GenericAPIView):
    """
    Returns the contact details.
    """
    permission_classes = [permissions.IsAuthenticated]
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
            message = []
            for field, er in form.errors.items():
                message.append(f"{field}: [{strip_tags(er)}]")
            response = ResponseMessage(ResponseMessage.ERROR, str(message))
            return Response({"response": response.to_json()}, status=400)


class GalleryAPI(generics.GenericAPIView):
    """
    Returns the contact details.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GallerySerializer
    form_class = GalleryForm

    def get(self, request, **kwargs):
        gallery = Gallery.objects.all().order_by("-created_at")

        data = self.serializer_class(gallery,
                                     context={
                                         "request": request
                                     },
                                     many=True).data
        return Response({"gallery": data})

    def post(self, request, **kwargs):
        form = self.form_class(request.data, request.FILES)
        if form.is_valid():
            item = form.save()
            data = self.serializer_class(item, context={
                "request": request
            }).data
            return Response({"item": data})
        else:
            # Return the first error.
            for field, er in form.errors.items():
                message = f"{field}: [{strip_tags(er)}]"
                response = ResponseMessage(ResponseMessage.ERROR, message)
                return Response({"response": response.to_json()})

    def patch(self, request, **kwargs):
        id = request.data.get("id")
        item  = generics.get_object_or_404(Gallery, id=id)
        form = self.form_class(request.data, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            data = self.serializer_class(item, context={
                "request": request
            }).data
            return Response({"item": data})
        else:
            # Return the first error.
            for field, er in form.errors.items():
                message = f"{field}: [{strip_tags(er)}]"
                response = ResponseMessage(ResponseMessage.ERROR, message)
                return Response({"response": response.to_json()})

    def delete(self, request, **kwargs):
        id = request.data.get("id")
        items = Gallery.objects.filter(id=id)
        data = self.serializer_class(items.first(), context={"request": request}).data
        items.delete()
        return Response({"item": data})
