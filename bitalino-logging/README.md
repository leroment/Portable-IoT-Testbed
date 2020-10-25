# Setup
## Installation

If on Windows, you will needs a specific version of the Windows SDK:
1. Install Windows SDK 10.0.18362.1 (Must have `Irprops.lib` meaning pre-19023)

This project requires [Python](https://www.python.org/) to run.

Steps:
1. Install Python
2. Install virtualenv
    - If on Windows, install `virtualenvwrapper-win` with `python -m pip install virtualenvwrapper-win`
    - If on Linux / OSX install `virtualenv` with `python -m pip install virtualenv`
3. Create virtual env `mkvirtualenv env`
4. Activate virtual env `workon env`
5. Run `python -m pip install -r requirements.txt`

If there are issues, try following installation instructions for the problematic packages. e.g. [PyBluez](https://github.com/pybluez/pybluez/blob/master/docs/install.rst)

## InfluxDB

This project was set up to use free InfluxDB Cloud 2.0, but could be adapted to work with other versions.

1. Sign up for an [InfluxDB account](https://cloud2.influxdata.com/signup)
2. Enter the organisation name in `Settings.InfluxDB.org` in [settings.py](settings.py)
    - This can also be found under your email when pressing the profile button on the sidebar.
3. Under the Data tab on the sidebar, select Buckets and `+ Create Bucket`
4. Select the bucket settings to meet your needs
5. Enter the name of the bucket into `Settings.InfluxDB.bucket` in [settings.py](settings.py)
6. Now select Tokens and press `+ Generate`
7. Name the token
8. Select only the bucket you just created under Write and then press Save
9. Press the newly created token
10. Copy to Clipboard and paste into `Settings.InfluxDB.token` in [settings.py](settings.py)
11. Change the region/start of `Settings.InfluxDB.url` in [settings.py](settings.py) to match the URL in your web browser

# Running

If running for the first time on Windows, you will need to allow the Bitalino bluetooth connection by clicking the `Set up device` notification.

1. Activate virtual env `workon env`
2. Ensure the InfluxDB details are set up correctly in `settings.py`
3. Ensure the desired sensors are plugged into the ports defined in `settings.py`
4. Run main script `python main.py`
5. Input your unique data tokens from the Health Monitoring dashboard. Data will not be logged for sensors you do not enter a token for.
6. Data will then start being logged.
