from pydantic import BaseModel
from datetime import date

class EmployeeCreate(BaseModel):

    name: str
    email: str
    phone: str
    department: str
    salary: int
    joining_date: date


class AttendanceCreate(BaseModel):

    employee_id: int
    date: date
    status: str