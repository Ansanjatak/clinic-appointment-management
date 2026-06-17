from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from models import Base


import users
import doctors
import appointments

app = FastAPI(
    title="Clinic Appointment Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(doctors.router)
app.include_router(appointments.router)

@app.get("/")
def home():
    return {
        "message":"Clinic Appointment Management System"
    }