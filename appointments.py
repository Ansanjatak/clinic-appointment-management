from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Appointment
from schemas import AppointmentCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/appointment")
def book_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db)
):

    new_appointment = Appointment(
    patient_name=appointment.patient_name,
    doctor_name=appointment.doctor_name,
    appointment_date=appointment.appointment_date,
    status="Confirmed"
)

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment


@router.get("/appointment")
def get_appointments(
    db: Session = Depends(get_db)
):
    return db.query(Appointment).all()

@router.delete("/appointment/{appointment_id}")
def delete_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):

    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id
    ).first()

    if not appointment:
        return {
            "message": "Appointment not found"
        }

    db.delete(appointment)
    db.commit()

    return {
        "message": "Appointment deleted"
    }