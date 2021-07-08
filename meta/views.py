from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OpeningHoursSerializer
from .models import OpeningHours


# Create your views here.
class OpeningHoursViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to receive the last visit number
    """
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursSerializer
    http_method_names = ['get']
