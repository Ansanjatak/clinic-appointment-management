from fastapi import APIRouter

router = APIRouter()

@router.post("/doctor")
def add_doctor():
    return {"message":"Doctor Added"}

@router.get("/doctor")
def get_doctors():
    return {"message":"Doctors List"}