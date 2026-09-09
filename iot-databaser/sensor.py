import requests
import random
import time

while True:
    value = round(random.uniform(20,30),1)
    humidity =round(random.uniform(30,70),1)

    requests.post(
        "http://localhost:5000/sensor-data",

        json={
            "device": "sensor1",
            "temp": value,
            "humidity": humidity
        }
    )

    print("Skickade:", value)
    time.sleep(5)