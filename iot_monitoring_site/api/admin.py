from django.contrib import admin
from .models import PatientData, ECGData, EDAData, EMGData, AccelerometerData, CriticalVitals

# Register your models here.

admin.site.register(PatientData)
admin.site.register(ECGData)
admin.site.register(EDAData)
admin.site.register(EMGData)
admin.site.register(AccelerometerData)