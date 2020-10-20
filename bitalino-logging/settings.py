class Settings:
    class InfluxDB:
        url = 'https://westeurope-1.azure.cloud2.influxdata.com'
        token = "az6A4sveVy8e-_q8s2aUyP-pYllkT5XQbdxLjRzyrjdNtRh5bw8kTXaQncCcmQ1vQ1O48ChFkOMynygWNY5xKg=="
        org = "andrew.a.cai@student.uts.edu.au"
        bucket = "andrew.a.cai's Bucket"

    influxdb = InfluxDB()

    class Bitalino:
        # The macAddress variable on Windows can be "XX:XX:XX:XX:XX:XX" or "COMX"
        # while on Mac OS can be "/dev/tty.BITalino-XX-XX-DevB" for devices ending with the last 4 digits of the MAC address or "/dev/tty.BITalino-DevB" for the remaining
        mac_address = '88:6B:0F:94:46:62'
        battery_led_threshold = 30  # 0 - 63 = 3.4v - 3.8v

    bitalino = Bitalino()

    class Sampling:
        base_sample_rate = 100  # Hz
        samples_per_read = 10

        ecg_rate = 10  # Hz
        acc_rate = 10  # Hz
        eda_rate = 10  # Hz
        emg_rate = 10  # Hz

        hr_buffer_seconds = 10
        hr_interval_seconds = 1


    sampling = Sampling()


settings = Settings()
