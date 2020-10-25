# Portable-IoT-Testbed Backend

## Running Django API
### Setup

1. Install Python
2. Install `virtualenvwrapper-win` with `python -m pip install virtualenvwrapper-win`
3. Navigate to Portable-IoT-Testbed/iot_monitoring_site folder in terminal
4. Run `mkvirtualenv iot_backend`
5. Run `workon iot_backend`
6. Run `python -m pip install -r requirements.txt`

### Running

1. Run `workon iot_backend`
2. Run `python manage.py runserver`


## Modules Used:
- Django
- Django rest framework
- Django rest knox
- DRF Nested Routers


## Endpoints
(all start with `/api`)

### Login
Get authentication token for user.

##### Format
```json
POST /api/login/
{
    "email": "<user email>",
    "password": "<user password>"
}
```

#### Responses
##### Successful response:
```json
200 OK
{
    "token": "<auth token>",
    "expiry": "<expiry>"
}
```

##### Invalid credentials
```json
400 Bad Request
{
    "non_field_errors": [
        "Unable to log in with provided credentials."
    ]
}
```

### Logout
Logout user.

##### Format
```json
POST /api/logout/
{
    "token": "<auth token>"
}
```

#### Responses
##### Successful response:
```json
200 OK
{

}
```

##### Invalid credentials
```json
400 Bad Request
{
    "detail": "Authentication credentials were not provided."
}
```

### Logout All
Logout user from all instances.

##### Format
```json
POST /api/logoutall/
{
    "token": "<auth token>"
}
```

#### Responses
##### Successful response:
```json
200 OK
{

}
```

##### Invalid credentials
```json
400 Bad Request
{
    "detail": "Authentication credentials were not provided."
}
```

### Register
Register a user.

##### Format
```json
POST /api/register/
{
    "username": "<username>",
    "email": "<email>",
    "password": "<password>"
}
```

#### Responses
##### Successful response:
```json
200 OK
{
    "user": {
        "id": <ID>,
        "username": "<username>",
        "email": "<email>",
        "is_staff": <true/false>
    },
    "token": "<auth-token>"
}
```

##### Invalid credentials
```json
400 Bad Request
{
    "email": [
        "Enter a valid email address."
    ]
}
```


### List Users/Patients/Health Officers
List Users/Patients/Health Officers.

##### Format
```json
GET /api/<users/patients/healthofficers>/
```

#### Responses
##### Successful response:
```json
200 OK
[
  {
      "id": <ID>,
      "username": "<username>",
      "email": "<email>",
      "is_staff": <true/false>
  },
  ...
 ]
```

### User/Patient/Health Officer
Obtain a User/Patient/Health Officer.

##### Format
```json
GET /api/<users/patients/healthofficers>/<ID>
```

#### Responses
##### Successful response:
```json
200 OK
{
    "id": <ID>,
    "username": "<username>",
    "email": "<email>",
    "is_staff": <true/false>
}
```

### ECG/EDA/EMG/Accelerometer
Obtain ECG/EDA/EMG/Accelerometer data.

##### Format
```json
GET /api/<ECG/EDA/EMG/Accelerometer>/<ID>
```

#### Responses
##### Successful response:
```json
200 OK
{
    "id": <ID>,
    "patient": <Patient_ID>,
    "data_id": <Data_ID>
}
```
##### Invalid credentials
```json
404 Not Found
{
    "detail": "Not found."
}
```

### Patient Data
Obtain patient data.

##### Format
```json
GET /api/patients/<ID>/patientdata
```

#### Responses
##### Successful response:
```json
200 OK
{
        "id": <ID>,
        "user": <User_id>,
        "health_officer": <HealthOfficer_Id>,
        "creation_date": <creation_date>,
        "ecg": [
            {
                "id": <ecg_id>,
                "patient_data": <patientdata_id>,
                "data_id": <data_id>
            }
        ],
        "eda": [
            {
                "id": <eda_id>,
                "patient_data": <patientdata_id>,
                "data_id": <data_id>
            }
        ],
        "emg": [
            {
                "id": <emg_id>,
                "patient_data": <patientdata_id>,
                "data_id": <data_id>
            }
        ],
        "accelerometer": [
            {
                "id": <accelerometer_id>,
                "patient_data": <patientdata_id>,
                "data_id": <data_id>
            }
        ]
    }
```
##### Invalid credentials
```json
404 Not Found
{
    "detail": "Not found."
}
```

