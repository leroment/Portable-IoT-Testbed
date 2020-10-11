from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from rest_framework import generics, permissions, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer, PatientDataSerializer, ECGDataSerializer, EDADataSerializer, EMGDataSerializer, AccelerometerDataSerializer
from .models import PatientData, ECGData, EDAData, EMGData, AccelerometerData, CriticalVitals

# Create your views here.

#def home(request):
#    return HttpResponse('<h1>Api home</h1>')


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
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

class PatientViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff = False)
    serializer_class = UserSerializer

class HealthOfficerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff = True)
    serializer_class = UserSerializer

class PatientDataViewSet(viewsets.ModelViewSet):
    queryset = PatientData.objects.all()
    serializer_class = PatientDataSerializer

class ECGDataViewSet(viewsets.ModelViewSet):
    queryset = ECGData.objects.all()
    serializer_class = ECGDataSerializer

class EDADataViewSet(viewsets.ModelViewSet):
    queryset = EDAData.objects.all()
    serializer_class = EDADataSerializer

class EMGDataViewSet(viewsets.ModelViewSet):
    queryset = EMGData.objects.all()
    serializer_class = EMGDataSerializer

class AccelerometerDataViewSet(viewsets.ModelViewSet):
    queryset = AccelerometerData.objects.all()
    serializer_class = AccelerometerDataSerializer

