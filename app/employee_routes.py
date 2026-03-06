from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models, schemas

router = APIRouter()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE EMPLOYEE
@router.post("/employees")
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):

    employee = models.Employee(**emp.dict())

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee


# GET EMPLOYEES
@router.get("/employees")
def get_employees(db: Session = Depends(get_db)):

    employees = db.query(models.Employee).all()

    return employees


# DELETE EMPLOYEE
@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):

    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()

    if not employee:
        return {"message": "Employee not found"}

    db.delete(employee)
    db.commit()

    return {"message": "Employee deleted successfully"}