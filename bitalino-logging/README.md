# Installation

If on Windows, you will needs a specific version of the Windows SDK:
1. Install Windows SDK 10.0.18362.1 (Must have `Irprops.lib` meaning pre-19023)

Then:
1. Create virtual env `mkvirtualenv env`
2. Activate virtual env `workon env`
3. Run `python -m pip install -r requirements.txt`

# Running

If running for the first time on Windows, you will need to allow the Bitalino bluetooth connection by clicking the `Set up device` notification.

1. Activate virtual env `workon env`
2. Run main script `python main.py`
3. Ensure the desired sensors are plugged into the ports defined in `settings.py`
3. Input your unique data tokens from the Health Monitoring dashboard. Data will not be logged for sensors you do not enter a token for.
4. Data will then start being logged.
