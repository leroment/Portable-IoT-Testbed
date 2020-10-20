from datetime import datetime, timedelta
from bitalino import BITalino, ExceptionCode
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import WriteType, WriteOptions
from settings import settings
from process import ECG, ACC, HR, EDA, EMG

import time
import signal
import logging

from log_config import configure_logging


logger = logging.getLogger()


def get_tokens():
    print("Enter your personal tokens from the Health Monitoring dashboard:")
    ecg_token = input('ECG Token:')
    acc_token = input('ACC Token:')
    emg_token = input('EMG Token:')
    eda_token = input('EDA Token:')

    return {
        'acc': acc_token,
        'ecg': ecg_token,
        'emg': emg_token,
        'eda': eda_token,
    }


def setup_influxdb():
    client = InfluxDBClient(url=settings.influxdb.url, token=settings.influxdb.token)

    # TODO decide on Batching or Asynchronous
    # if high sample rate, go with batching,
    # if low, probs go async as it should be able to handle it
    write_api = client.write_api(write_options=WriteOptions(
        write_type=WriteType.batching,
        batch_size=100,
    ))

    return (client, write_api)


def start_device():
    # Connect to BITalino
    device = BITalino(settings.bitalino.mac_address)

    # Set battery threshold
    device.battery(settings.bitalino.battery_led_threshold)

    # Read BITalino version
    logger.info(device.version())

    # Start Acquisition
    device.start(settings.sampling.base_sample_rate, [0, 1, 2, 3])

    return device


def stop_device(device):
    logger.info('Terminating device connection')

    # Stop acquisition
    device.stop()

    # Close connection
    device.close()



def run_logging(device, write_api, data_tokens):
    subsample_data = {
        'acc': [],
        'ecg': [],
        'emg': [],
        'eda': [],
        'hr': [],
    }

    cancel = False

    def keyboard_interrupt_handler(*args):
        nonlocal cancel
        cancel = True

    signal.signal(signal.SIGINT, keyboard_interrupt_handler)

    sample_time = datetime.utcnow()
    time_between_samples = timedelta(seconds=1) / settings.sampling.base_sample_rate
    while not cancel:
        while True:
            try:
                data = device.read(settings.sampling.samples_per_read)
                break
            except ExceptionCode.CONTACTING_DEVICE:
                logger.error('Bitalino device disconnected, retrying in 5 seconds')
                time.sleep(5)

        points = []
        for data_point in data:
            ECG(subsample_data['ecg'], points, sample_time, data_point, data_tokens['ecg'])
            ACC(subsample_data['acc'], points, sample_time, data_point, data_tokens['acc'])
            HR(subsample_data['hr'], points, sample_time, data_point, data_tokens['ecg'])  # use ecg token as ECG and HR go hand in hand
            EDA(subsample_data['eda'], points, sample_time, data_point, data_tokens['eda'])
            EMG(subsample_data['emg'], points, sample_time, data_point, data_tokens['emg'])

            sample_time = sample_time + time_between_samples

        write_api.write(settings.influxdb.bucket, settings.influxdb.org, points)


def run():
    configure_logging()

    tokens = get_tokens()
    client, write_api = setup_influxdb()

    device = start_device()

    run_logging(device, write_api, tokens)

    stop_device(device)


if __name__ == "__main__":
    run()
