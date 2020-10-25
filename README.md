# IoT Health Monitoring System

## BITalino Logging

This section of the project is responsible for reading data from the BITalino hardware and sending it to the InfluxDB database.

Please find instructions on how to install and run it in [bitalino-logging/README.md](bitalino-logging/README.md). Instructions on setting up InfluxDB are also included.


## Frontend website

This section of the project is responsible for providing the website for the dashboard to manage users and view real-time data.

Please find instructions on how to install and run it in [frontend/readme.md](frontend/readme.md).


### Grafana

The dashboard uses [Grafana](https://grafana.com/) to display the real-time data from InfluxDB. Each panel must be created prior to running the website by importing the files inside the `grafana` folder.

Please find instructions on how to do this in [grafana/README.md](grafana/README.md).


## Backend API

This section of the project is responsible for providing the API for the web dashboard.

Please find instructions on how to install and run it in [iot_monitoring_site/README.md](iot_monitoring_site/README.md). The available endpoints are also documented here.
