from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# MARK ATTENDANCE
@router.post("/attendance")
def mark_attendance(data: schemas.AttendanceCreate, db: Session = Depends(get_db)):

    existing = db.query(models.Attendance).filter(
        models.Attendance.employee_id == data.employee_id,
        models.Attendance.date == data.date
    ).first()

    if existing:
        existing.status = data.status
        db.commit()
        db.refresh(existing)
        return {"message": "Attendance updated", "attendance": existing}

    attendance = models.Attendance(**data.dict())

    db.add(attendance)
    db.commit()
    db.refresh(attendance)

    return {"message": "Attendance marked", "attendance": attendance}


# GET ALL ATTENDANCE
@router.get("/attendance")
def get_attendance(db: Session = Depends(get_db)):
    return db.query(models.Attendance).all()


# GET ATTENDANCE BY EMPLOYEE
@router.get("/attendance/{employee_id}")
def get_employee_attendance(employee_id: int, db: Session = Depends(get_db)):

    records = db.query(models.Attendance).filter(
        models.Attendance.employee_id == employee_id
    ).all()

    return records