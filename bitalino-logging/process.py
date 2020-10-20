import neurokit2 as nk
import numpy as np
import logging

from influxdb_client import Point, WritePrecision
from settings import settings

logger = logging.getLogger()

'''
ECG
'''

ecg_full_buffer_count = int(settings.sampling.base_sample_rate / settings.sampling.ecg_rate)


def ECG(subsample_data, points, sample_time, data_point, token):
    if not token:
        return

    subsample_data.append(data_point[5])
    if len(subsample_data) == ecg_full_buffer_count:
        sampled = np.max(subsample_data)  # use max to show peaks
        subsample_data.clear()

        points.append(
            Point("TIM-DEV")
            .tag("type", 'ECG')
            .tag("token", token)
            .field("voltage", sampled)
            .time(sample_time, WritePrecision.NS)
        )
        logger.info(f'ECG: {sampled}')


'''
Accelerometer
'''

acc_full_buffer_count = int(settings.sampling.base_sample_rate / settings.sampling.acc_rate)

def acc_to_g(val):
    c_min = 420
    c_max = 624
    return (((val - c_min) / (c_max - c_min)) * 2) - 1


def ACC(subsample_data, points, sample_time, data_point, token):
    if not token:
        return

    subsample_data.append(data_point[6])
    if len(subsample_data) == acc_full_buffer_count:
        sampled = np.max(subsample_data)  # use max to show peaks
        subsample_data.clear()

        points.append(
            Point("TIM-DEV")
            .tag("type", 'ACC')
            .tag("token", token)
            .field("g", acc_to_g(sampled))
            .time(sample_time, WritePrecision.NS)
        )
        logger.info(f'ACC: {sampled} {acc_to_g(sampled):.3f}m/s²')


'''
Heart Rate
'''

hr_full_buffer_count = settings.sampling.base_sample_rate * settings.sampling.hr_buffer_seconds
hr_delete_count = settings.sampling.base_sample_rate * settings.sampling.hr_interval_seconds


def process_hr(data):
    signals, info = nk.ecg_process(data, sampling_rate=100)
    return np.mean(signals['ECG_Rate'])


def HR(subsample_data, points, sample_time, data_point, token):
    if not token:
        return

    subsample_data.append(data_point[5])

    if len(subsample_data) >= hr_full_buffer_count:
        hr = process_hr(subsample_data)
        del subsample_data[:hr_delete_count]

        points.append(
            Point("TIM-DEV")
            .tag("type", 'HR')
            .tag("token", token)
            .field("bpm", hr)
            .time(sample_time, WritePrecision.NS)
        )
        logger.info(f'Heart Rate: {hr}')
