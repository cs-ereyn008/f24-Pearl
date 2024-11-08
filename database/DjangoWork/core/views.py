from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import User, TrafficLaw, Violation
from .serializers import UserSerializer, TrafficLawSerializer, ViolationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TrafficLawViewSet(viewsets.ModelViewSet):
    queryset = TrafficLaw.objects.all()
    serializer_class = TrafficLawSerializer

class ViolationViewSet(viewsets.ModelViewSet):
    queryset = Violation.objects.all()
    serializer_class = ViolationSerializer