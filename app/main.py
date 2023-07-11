"""
Main file for XYZ API Application
"""
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Main API Method"""
    time = datetime.timestamp(datetime.now())
    return {"message": "Automate all the things!", "timestamp": time}
