import requests
import pandas as pd
import os
import random

import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

os.environ["INFLUXDB_TOKEN"] = "PLgoxmctBijyFzpWtIWosAL_moVzoV77RlLM0hFdtjsiE13znrZwxu60r5XNkOx2H51fYnD1wBLVYivpIusNaA=="

token = os.environ.get("INFLUXDB_TOKEN")
org = "HSLU"
url = "http://localhost:8086"

bucket = "BaseData"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
write_api = write_client.write_api(write_options=SYNCHRONOUS)

counter = 0

try:
    while counter < 100:
        # Simulated sensor values
        vibration = round(random.uniform(0.1, 1.5), 2)  # Rounded to 2 decimals
        temperature = round(random.uniform(40, 80), 2)

        # 🔹 Corrected Data Format (Using Point)
        point = (
            Point("pumpe")
            .tag("maschine", "Pumpe1")
            .field("vibration", vibration)
            .field("temperatur", temperature)
        )

        # Write to InfluxDB
        write_api.write(bucket=bucket, org=org, record=point)
        print(f"Gespeichert: Vibration={vibration}, Temperatur={temperature}°C")
        counter += 1

        time.sleep(10)  # Wait 10 seconds before next data point

except KeyboardInterrupt:
    print("\n Messung beendet (CTRL+C gedrückt).")

finally:
    write_client.close()