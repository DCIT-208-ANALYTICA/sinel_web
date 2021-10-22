from rest_framework import serializers
from accounts.models import Administrator
from django.contrib.auth import authenticate


class AdministratorSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    def get_photo(self, administrator):
        request = self.context.get("request")
        url = administrator.photo.url
        return request.build_absolute_uri(url)

    class Meta:
        model = Administrator
        exclude = [
            "id",
            "created_at",
            "password",
            "is_staff",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = [
            "id",
            "fullname",
            "password",
            "photo",
            "email_address",
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            },
            "id": {
                "read_only": True
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email_address = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
