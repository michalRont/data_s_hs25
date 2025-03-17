from influxdb import InfluxDBClient
import Adafruit_DHT
import time

# InfluxDB Verbindung
client = InfluxDBClient(host='localhost', port=8086, database='sensor_data')

sensor = Adafruit_DHT.DHT22
pin = 4  # GPIO-Pin für den Sensor

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
        data = [
            {
                "measurement": "raumklima",
                "tags": {"raum": "Büro1"},
                "fields": {"temperatur": temperature, "luftfeuchte": humidity}
            }
        ]
        client.write_points(data)
        print(f"Gespeichert: Temp={temperature}°C, Feuchte={humidity}%")
    
    time.sleep(10)  # 