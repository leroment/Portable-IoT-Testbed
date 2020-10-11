Running Django API
Setup

1. Install Python
2. Install virtualenvwrapper-win with python -m pip install virtualenvwrapper-win
3. Navigate to Portable-IoT-Testbed/iot_monitoring_site folder in terminal
4. Run mkvirtualenv iot_backend
5. Run workon iot_backend
6. Run python -m pip install -r requirements.txt

Running

1. Run workon iot_backend
2. Run python manage.py runserver


Modules Used:
- Django
- Django rest framework
- Django rest knox
- DRF Nested Routers


Routes
- /api/login
- /api/logout
- /api/logoutall
- /api/register
- /api/users
- /api/users/{pk}
- /api/patients/
- /api/patients/{pk}
- /api/patients/{pk}/patientdata
- /api/patients/{pk}/patientdata/{pk}
- /api/healthofficers/
- /api/healthofficers/{pk}
- /api/ecg/
- /api/ecg/{pk}
- /api/eda/
- /api/eda/{pk}
- /api/emg/
- /api/emg/{pk}
- /api/accelerometer/
- /api/accelerometer/{pk}
