from rest_framework import generics, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from accounts.api_v1.serializers import (AdministratorSerializer,
                                         ChangeAdministratorPasswordSerializer,
                                         LoginSerializer, RegisterSerializer)
from accounts.forms import AdministratorForm
from accounts.models import Administrator
from knox.models import AuthToken
from django.contrib.auth import authenticate


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
    """An API end point to allow registered administrators to login"""

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
    permission_classes = [permissions.IsAuthenticated]
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


class RetrieveAdministrator(generics.GenericAPIView):
    """
    Returns the details of an administrator.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdministratorSerializer

    def get(self, request, email_address, **kwargs):
        administrator = generics.get_object_or_404(Administrator,
                                                   email_address=email_address)
        data = self.serializer_class(administrator,
                                     context={
                                         "request": request
                                     }).data
        return Response({"administrator": data})


class MyAccount(generics.GenericAPIView):
    """
    Returns the details of an administrator.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdministratorSerializer

    def get(self, request, **kwargs):
        data = self.serializer_class(request.user,
                                     context={
                                         "request": request
                                     }).data
        return Response({"administrator": data})


class ChangeAdministratorPasswordApi(generics.GenericAPIView):
    """
    Change the password of an administrator.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangeAdministratorPasswordSerializer

    def post(self, request, **kwargs):
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        email_address = request.data.get("email_address")

        administrator = generics.get_object_or_404(Administrator,
                                                   email_address=email_address)

        if request.user.is_superuser:
            administrator.set_password(new_password)
            administrator.save()
        elif request.user.email_address == email_address:
            administrator = authenticate(email_address=email_address,
                                         password=old_password)
            if administrator:
                administrator.set_password(new_password)
                administrator.save()
            else:
                response_data = {
                    "error_message": "Incorrect credentials.",
                    "user": None,
                    "token": None,
                }
                return Response({"response": response_data},
                                status=status.HTTP_401_UNAUTHORIZED)

        # Delete old tokens e.g., invalid all logged in accounts.
        AuthToken.objects.filter(user=administrator).delete()
        response_data = {
            "error_message":
            None,
            "administrator":
            AdministratorSerializer(
                administrator,
                context={
                    "request": request
                },
            ).data,
            "token":
            AuthToken.objects.create(administrator)[1],
        }
        return Response({"response": response_data}, status=status.HTTP_200_OK)
