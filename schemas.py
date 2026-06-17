from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    fullname: str
    email: str
    password: str

class DoctorCreate(BaseModel):
    doctor_name: str
    specialization: str

class AppointmentCreate(BaseModel):
    patient_name: str
    doctor_name: str
    appointment_date: date
    
class LoginUser(BaseModel):
    email: str
    password: str