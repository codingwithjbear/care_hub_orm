# serializers.py
from rest_framework import serializers
from .models import Patient, HealthData

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class HealthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthData
        fields = '__all__'