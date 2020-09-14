import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import csv


bucket = "6155c521eefc55c4"
org = "7c5f3c719b78efbf"
token = "KjYvccIZbEZPMHukns-1n2cFYwHnHB8oVwFaYhNZH3tmMwNCQM9nxVokxSNq48aVwkIM4CE6PtFIefIL8l_SEw=="
# Store the URL of your InfluxDB instance
url = "https://westeurope-1.azure.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

with open('ecg2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        p = influxdb_client.Point("ecg_measurement").tag(
            "patient", "andrew_cai").field("reading", int(row[2]))
        write_api.write(bucket=bucket, org=org, record=p)
        print("write " + row[2])
