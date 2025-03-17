import requests
import pandas as pd
import os

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
   
for value in range(5):
  point = (
    Point("testMeasure1")
    .tag("testTag1", "testValue1")
    .field("testField1", value)
  )
  write_api.write(bucket=bucket, org="HSLU", record=point)
  time.sleep(1)



