# Grafana Setup

## Set up Linux/Debian VM on Google Cloud

We used Google Cloud to setup our Grafana instance.

On Google Cloud, we created an Linux/Debian VM. Instructions to setup a VM on Google Cloud can be found in the following link:
[https://cloud.google.com/compute/docs/quickstart-linux]

## Set up Grafana instance

1. Open terminal
2. Run `sudo apt-get update https://packages.grafana.com/oss/deb stable main`
3. Start the server by running `sudo systemctl start grafana-server`

Please refer to [https://grafana.com/docs/grafana/latest/installation/debian/] for more information about setting up a Grafana instance.

## Import Dashboard

1. To import a dashboard click the + icon in the side menu, and then click Import.
2. From here you can upload a dashboard JSON file, paste a Grafana.com dashboard URL or paste dashboard JSON text directly into the text area.
3. In step 2 of the import process Grafana will let you change the name of the dashboard, pick what data source you want the dashboard to use and specify any metric prefixes (if the dashboard use any).

Please refer to [https://grafana.com/docs/grafana/latest/dashboards/export-import/] for more information about importing dashboards.
