from django.shortcuts import render

from rest_framework import generics

from .models import Avalanche_Accident
from .serializers import Avalanche_AccidentSerializer

class ListAvalanche_Accident(generics.ListCreateAPIView):
    queryset = Avalanche_Accident.objects.all()
    serializer_class = Avalanche_AccidentSerializer

class DetailAvalanche_Accident(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avalanche_Accident.objects.all()
    