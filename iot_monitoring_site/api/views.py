from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from rest_framework import generics, permissions, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth.models import User
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
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

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


