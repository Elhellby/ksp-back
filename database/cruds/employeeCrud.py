from datetime import datetime
from sqlalchemy.orm import Session
from models.employeeModel import Employee as EmployeeModel
from database.schemas.employeeSchema import Employee as EmployeeSchema


def get(db: Session, skip: int = 0, limit: int = 100):
    return db.query(EmployeeModel).filter(EmployeeModel.Status==True).offset(skip).limit(limit).all()


def get_id(db: Session, employee_id: int):
    return db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()


def post(db: Session, employee: EmployeeSchema):
    _employee = EmployeeModel(
        Picture=employee.picture,
        Name=employee.name,
        Position=employee.position,
        Salary=employee.salary,
        Status=True,
        CreationDate=datetime.now()
    )
    db.add(_employee)
    db.commit()
    db.refresh(_employee)
    return _employee


def update(db: Session, employee: EmployeeSchema):
    _employee = get_id(db, employee.id)

    _employee.Picture = employee.picture
    _employee.Name = employee.name
    _employee.Position = employee.position
    _employee.Salary = employee.salary

    db.commit()
    db.refresh(_employee)
    return _employee

def delete(db: Session, employeeId: int):
    _employee = get_id(db, employeeId)

    _employee.Status = False

    db.commit()
    db.refresh(_employee)
    return _employee
