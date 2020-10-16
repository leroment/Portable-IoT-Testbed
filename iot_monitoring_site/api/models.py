from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PatientData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_data')
    health_officer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='health_officer_id')
    creation_date = models.DateTimeField(auto_now_add=True)

class ECGData(models.Model):
    patient_data = models.ForeignKey(PatientData, on_delete=models.CASCADE)
    data_id = models.FloatField()

class EDAData(models.Model):
    patient_data = models.ForeignKey(PatientData, on_delete=models.CASCADE)
    data_id = models.FloatField()

class EMGData(models.Model):
    patient_data = models.ForeignKey(PatientData, on_delete=models.CASCADE)
    data_id = models.FloatField()

class AccelerometerData(models.Model):
    patient_data = models.ForeignKey(PatientData, on_delete=models.CASCADE)
    data_id = models.FloatField()

class CriticalVitals(models.Model):
    patient_data = models.ForeignKey(PatientData, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2048, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    #paramedic = models.ForeignKey(User, on_delete=models.PROTECT)
    resolved = models.BooleanField()

