from fastapi import FastAPI

import users
import doctors
import appointments

app = FastAPI(
    title="Clinic Appointment Management System"
)

app.include_router(users.router)
app.include_router(doctors.router)
app.include_router(appointments.router)

@app.get("/")
def home():
    return {
        "message":"Clinic Appointment Management System"
    }