from django.conf.urls import include
from django.urls import path
from knox import views as knox_views
from rest_framework import routers
from rest_framework_nested import routers
from .views import (
    RegisterAPI, 
    LoginAPI, 
    UserViewSet, 
    PatientViewSet, 
    HealthOfficerViewSet,
    DataViewSet,
    PatientDataViewSet, 
    ECGDataViewSet, 
    EDADataViewSet, 
    EMGDataViewSet, 
    AccelerometerDataViewSet,
    CustomObtainAuthToken
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'datalist', DataViewSet)
router.register(r'healthofficers', HealthOfficerViewSet)
router.register(r'ecg', ECGDataViewSet)
router.register(r'eda', EDADataViewSet)
router.register(r'emg', EMGDataViewSet)
router.register(r'accelerometer', AccelerometerDataViewSet)

patients_router = routers.NestedSimpleRouter(router, r'patients', lookup='user')
patients_router.register(r'patientdata', PatientDataViewSet, basename='patient-data')

urlpatterns = [
    #path('', views.home, name='api-home'),
    path(r'register', RegisterAPI.as_view(), name='register'),
    path(r'login', LoginAPI.as_view(), name='login'),
    path(r'logout', knox_views.LogoutView.as_view(), name='logout'),
    path(r'logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path(r'authenticate', CustomObtainAuthToken.as_view(), name='authenticate'),
    path(r'', include(router.urls)),
    path(r'', include(patients_router.urls)),

]