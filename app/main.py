from datetime import datetime
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    time = datetime.timestamp(datetime.now())
    return {"message": "Automate all the things!", "timestamp": time}
