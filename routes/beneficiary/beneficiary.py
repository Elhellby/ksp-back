from fastapi import APIRouter, Depends
from database.manager import SessionLocal
from sqlalchemy.orm import Session
from database.schemas.beneficiarySchema import RequestBeneficiary
from database.cruds.beneficiaryCrud import get, post, update, delete
from models.responseBase import ResponseBase


router = APIRouter(prefix="/api/beneficiary")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def GET(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _beneficiary = get(db, 0, 100)
    return ResponseBase(status="OK",
                        code=200,
                        message="Success",
                        data=_beneficiary).dict(exclude_none=True)


@router.post("")
async def POST(request: RequestBeneficiary, db: Session = Depends(get_db)):
    _beneficiary = post(db, beneficiary=request.parameter)
    return ResponseBase(status="Ok",
                        code="200",
                        message="Beneficiary created successfully with id "+str(_beneficiary.id)).dict(exclude_none=True)


@router.post("")
async def POST(request: RequestBeneficiary, db: Session = Depends(get_db)):
    _beneficiary = post(db, beneficiary=request.parameter)
    return ResponseBase(status="Ok",
                        code="200",
                        message="Beneficiary created successfully with id "+str(_beneficiary.id)).dict(exclude_none=True)


@router.patch("")
async def PATCH(request: RequestBeneficiary, db: Session = Depends(get_db)):
    _beneficiary = update(db, beneficiary=request.parameter)
    return ResponseBase(status="Ok",
                        code="200",
                        message="Success update data",
                        result=_beneficiary)


@router.delete("/{id}")
async def DELETE(id: int,  db: Session = Depends(get_db)):
    delete(db, beneficiaryId=id)
    return ResponseBase(status="Ok",
                        code="200",
                        message="Success delete beneficiary").dict(exclude_none=True)
