from sqlalchemy import *
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    email = Column(String)
    password = Column(String)

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    doctor_name = Column(String)
    specialization = Column(String)

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    patient_name = Column(String)
    doctor_name = Column(String)
    appointment_date = Column(Date)

    status = Column(String, default="Pending")