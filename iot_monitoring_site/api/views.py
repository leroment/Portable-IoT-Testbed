from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from rest_framework import generics, permissions, viewsets, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth.models import User
import uuid

from .serializers import UserSerializer, RegisterSerializer, PatientDataSerializer, ECGDataSerializer, EDADataSerializer, EMGDataSerializer, AccelerometerDataSerializer
from .models import PatientData, ECGData, EDAData, EMGData, AccelerometerData, CriticalVitals

# Create your views here.

class UserOnly(BasePermission):
    message = 'Invalid user'

    def has_permission(self, request, view):
        user_id = int(request.resolver_match.kwargs['user_pk'])
        return request.user.id == user_id


# Register API
class RegisterAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        patientdata = PatientData.objects.create(
            user_id = user.id,
            health_officer = User.objects.filter(is_staff = True).first(),
        )

        def id_generator():
            while True:
                data_id = str(uuid.uuid4())

                if not (ECGData.objects.filter(data_id=data_id).exists() and 
                        EDAData.objects.filter(data_id=data_id).exists() and
                        EMGData.objects.filter(data_id=data_id).exists() and
                        AccelerometerData.objects.filter(data_id=data_id).exists()):
                    return data_id

        ecg = ECGData.objects.create(
            patient_data = patientdata,
            data_id = id_generator(),
        )

        eda = ECGData.objects.create(
            patient_data = patientdata,
            data_id = id_generator(),
        )

        emg = EMGData.objects.create(
            patient_data = patientdata,
            data_id = id_generator(),
        )

        accelerometer = AccelerometerData.objects.create(
            patient_data = patientdata,
            data_id = id_generator(),
        )

        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1],
        "patient_data": patientdata.id,
        "ecg": ecg.data_id,
        "eda": eda.data_id,
        "emg": emg.data_id,
        "accelerometer": accelerometer.data_id
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, )


class PatientViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff = False)
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, )


class HealthOfficerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff = True)
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

#all data
class DataViewSet(viewsets.ModelViewSet):
    queryset = PatientData.objects.all()
    serializer_class = PatientDataSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, )

    def create(self, request, *args, **kwargs):
        validation_errors = {}

        data = None

        try:
            data = json.loads(request.data.get('data'))
        except TypeError:
            validation_errors['data'] = 'Must be JSON'

        healthofficer_id = int(self.kwargs['user_pk'])
        patient_id = data['patient_id']
        ecg_id = data['ecg']
        eda_id = data['eda']
        emg_id = data['emg']
        accelerometer_id = data['accelerometer']

        patientdata = PatientData.objects.create(
            user_id = patient_id,
            health_officer = healthofficer_id,
        )
        ecg = ECGData.objects.create(
            patient_data = patientdata,
            data_id = ecg_id,
        )
        eda = ECGData.objects.create(
            patient_data = patientdata,
            data_id = eda_id,
        )
        emg = EMGData.objects.create(
            patient_data = patientdata,
            data_id = emg_id,
        )
        accelerometer = AccelerometerData.objects.create(
            patient_data = patientdata,
            data_id = accelerometer_id,
        )

        response_data = {
            'id': patientdata.id,
            'ecg_id': ecg.id,
            'eda_id': eda.id,
            'emg_id': emg.id,
            'accelerometer_id': accelerometer.id
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

#single patient
class PatientDataViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDataSerializer
    permission_classes = (permissions.IsAuthenticated, UserOnly)

    def get_queryset(self):
        user_id = int(self.kwargs['user_pk'])
        return PatientData.objects.filter(user=user_id)
    


class ECGDataViewSet(viewsets.ModelViewSet):
    queryset = ECGData.objects.all()
    serializer_class = ECGDataSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)


class EDADataViewSet(viewsets.ModelViewSet):
    queryset = EDAData.objects.all()
    serializer_class = EDADataSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)


class EMGDataViewSet(viewsets.ModelViewSet):
    queryset = EMGData.objects.all()
    serializer_class = EMGDataSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)


class AccelerometerDataViewSet(viewsets.ModelViewSet):
    queryset = AccelerometerData.objects.all()
    serializer_class = AccelerometerDataSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)


