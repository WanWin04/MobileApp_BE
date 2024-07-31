from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    EmailField,
)
from account.models import DriverUser


class RegisterSerializer(serializers.ModelSerializer):
    email = EmailField(label="Email address")
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = DriverUser
        fields = [
            'id',
            'username',
            'email',
            'password',
            'confirm_password',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
            'id': {'read_only': True},
        }


    def validate_email(self, value):
        email = value
        user_qs = DriverUser.objects.filter(email=email)

        if user_qs.exists():
            raise ValidationError("Email already registered")

        return value


    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise ValidationError("Passwords do not match")
        return data


    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = DriverUser(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
