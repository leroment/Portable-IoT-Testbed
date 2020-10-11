from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PatientData, ECGData, EDAData, EMGData, AccelerometerData, CriticalVitals

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class PatientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientData
        fields = ('id', 'user', 'health_officer')

class ECGDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECGData
        fields = ('id', 'patient', 'data_id')

class EDADataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EDAData
        fields = ('id', 'patient', 'data_id')

class EMGDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EMGData
        fields = ('id', 'patient', 'data_id')

class AccelerometerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccelerometerData
        fields = ('id', 'patient', 'data_id')

