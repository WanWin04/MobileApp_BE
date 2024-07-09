from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from account.models import DriverUser


class Register(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    queryset = DriverUser.objects.all()
