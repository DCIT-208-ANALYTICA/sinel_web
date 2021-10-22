from rest_framework import generics, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from accounts.api_v1.serializers import AdministratorSerializer, LoginSerializer, RegisterSerializer
from accounts.forms import AdministratorForm
from accounts.models import Administrator
from rest_api_v1.utils import ResponseMessage
from django.utils.html import strip_tags
from knox.models import AuthToken


class RegisterAdministrator(generics.GenericAPIView):
    """An API enpoint to enabler new administrators to register."""

    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        error_message = ""
        request_data = request.data.copy()
        serializer = self.get_serializer(data=request_data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            for field in list(e.detail):
                error_message = e.detail.get(field)[0]
                response_data = {
                    "error_message": error_message,
                    "user": None,
                    "token": None,
                }
                return Response({"response": response_data},
                                status=status.HTTP_200_OK)
        user = serializer.save()
        response_data = {
            "error_message":
            None,
            "administrator":
            AdministratorSerializer(
                user,
                context={
                    "request": request
                },
            ).data,
            "token":
            AuthToken.objects.create(user)[1],
        }
        return Response({"response": response_data}, status=status.HTTP_200_OK)


class LoginAdministratorApi(generics.GenericAPIView):
    """An API end point to allow already registered users to login to ther mobile app."""

    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            for field in list(e.detail):
                error_message = e.detail.get(field)[0]
                response_data = {
                    "error_message": error_message,
                    "user": None,
                    "token": None,
                }
                return Response({"response": response_data},
                                status=status.HTTP_200_OK)

        user = serializer.validated_data
        response_data = {
            "error_message":
            None,
            "administrator":
            AdministratorSerializer(
                user,
                context={
                    "request": request
                },
            ).data,
            "token":
            AuthToken.objects.create(user)[1],
        }
        return Response({"response": response_data}, status=status.HTTP_200_OK)


class AdministratorsApi(generics.GenericAPIView):
    """
    Returns the list of all administrators
    """
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdministratorSerializer
    form_class = AdministratorForm

    def get(self, request, **kwargs):
        administrators = Administrator.objects.all()
        data = self.serializer_class(administrators,
                                     context={
                                         "request": request
                                     },
                                     many=True).data
        return Response({"administrators": data})


class AdministratorApi(generics.GenericAPIView):
    """
    Returns the list of all administrators
    """
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdministratorSerializer

    def get(self, request, admin_id, **kwargs):
        administrator = generics.get_object_or_404(Administrator, id=admin_id)
        data = self.serializer_class(administrator,
                                     context={
                                         "request": request
                                     }).data
        return Response({"administrator": data})
