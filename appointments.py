from fastapi import APIRouter

router = APIRouter()

@router.post("/appointment")
def book_appointment():
    return {"message":"Appointment Booked"}

@router.get("/appointment")
def get_appointments():
    return {"message":"Appointments List"}