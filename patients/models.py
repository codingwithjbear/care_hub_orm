from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    doctor = models.CharField(max_length=100)
    
class HealthData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    oxygen_level = models.IntegerField()
    heart_rate = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)