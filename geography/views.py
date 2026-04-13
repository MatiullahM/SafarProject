from django.shortcuts import render
from .models import Provinces, Terminals
from .serializers import ProvincesSerializer, TerminalsSerializer
from rest_framework import viewsets

# Create your views here.

class ProvincesViewSet(viewsets.ModelViewSet):
    queryset = Provinces.objects.all()
    serializer_class = ProvincesSerializer

class TerminalsViewSet(viewsets.ModelViewSet):
    queryset = Terminals.objects.all()
    serializer_class = TerminalsSerializer