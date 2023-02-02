from fastapi import APIRouter, Depends
from database.manager import SessionLocal
from sqlalchemy.orm import Session
from database.schemas.employeeSchema import RequestEmployee
from database.cruds.employeeCrud import get, post, update, delete
from models.responseBase import ResponseBase


router = APIRouter(prefix="/api/employee")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def GET(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _employee = get(db, 0, 100)
    return ResponseBase(status="OK",
                        code=200,
                        message="Success",
                        data=_employee).dict(exclude_none=True)


@router.post("")
async def POST(request: RequestEmployee, db: Session = Depends(get_db)):
    _employee = post(db, employee=request.parameter)
    return ResponseBase(status="Ok",
                        code="200",
                        message="Employee created successfully with id "+str(_employee.id)).dict(exclude_none=True)


@router.post("")
async def POST(request: RequestEmployee, db: Session = Depends(get_db)):
    _employee = post(db, employee=request.parameter)
    return ResponseBase(status="Ok",
                        code="200",
                        message="Employee created successfully with id "+str(_employee.id)).dict(exclude_none=True)


@router.patch("")
async def PATCH(request: RequestEmployee, db: Session = Depends(get_db)):
    _employee = update(db, employee=request.parameter)
    return ResponseBase(status="Ok",
                        code="200",
                        message="Success update data",
                        result=_employee)


@router.delete("/{id}")
async def delete_book(id: int,  db: Session = Depends(get_db)):
    delete(db, employeeId=id)
    return ResponseBase(status="Ok",
                        code="200",
                        message="Success delete employee").dict(exclude_none=True)
