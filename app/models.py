from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    department = Column(String(50))
    salary = Column(Integer)
    joining_date = Column(Date)


class Attendance(Base):

    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    date = Column(Date)
    status = Column(String(20))