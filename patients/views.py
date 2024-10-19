# views.py
from rest_framework import viewsets
from .models import Patient, HealthData
from .serializers import PatientSerializer, HealthDataSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class HealthDataViewSet(viewsets.ModelViewSet):
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer