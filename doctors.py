from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Doctor
from schemas import DoctorCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/doctor")
def add_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_db)
):
    new_doctor = Doctor(
        doctor_name=doctor.doctor_name,
        specialization=doctor.specialization
    )

    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    return new_doctor


@router.get("/doctor")
def get_doctors(
    db: Session = Depends(get_db)
):
    return db.query(Doctor).all()