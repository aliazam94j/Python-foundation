from fastapi import FastAPI
# http://127.0.0.1:8000
Sensor = FastAPI()

@Sensor.get("/")
def home():
    return {"Data":"Testing"} 




