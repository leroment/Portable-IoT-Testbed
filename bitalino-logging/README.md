# Installation

If on Windows, you will needs a specific version of the Windows SDK:
1. Install Windows SDK 10.0.18362.1 (Must have `Irprops.lib` meaning pre-19023)

Then:
1. Create virtual env `mkvirtualenv env`
2. Activate virtual env `workon env`
3. Run `python -m pip install -r requirements.txt`

# Running

1. Activate virtual env `workon env`
2. Run main script `python example.py`

If running for the first time on Windows, you will need to allow the Bitalino bluetooth connection by clicking the `Set up device` notification.
