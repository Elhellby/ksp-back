from datetime import datetime
from sqlalchemy.orm import Session
from models.beneficiaryModel import Beneficiary as BeneficiaryModel
from database.schemas.beneficiarySchema import Beneficiary as BeneficiarySchema


def get(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BeneficiaryModel).offset(skip).limit(limit).all()


def get_id(db: Session, beneficiary_id: int):
    return db.query(BeneficiaryModel).filter(BeneficiaryModel.id == beneficiary_id).first()


def post(db: Session, beneficiary: BeneficiarySchema):
    _beneficiary = BeneficiaryModel(
        FullName=beneficiary.fullName,
        Relationship=beneficiary.relationship,
        Gender=beneficiary.gender,
        Birthday=beneficiary.birthday,
        IdEmployee=beneficiary.idEmployee
    )
    db.add(_beneficiary)
    db.commit()
    db.refresh(_beneficiary)
    return _beneficiary


def update(db: Session, beneficiary: BeneficiarySchema):
    _beneficiary = get_id(db, beneficiary.id)
    _beneficiary.FullName = beneficiary.fullName
    _beneficiary.Relationship = beneficiary.relationship
    _beneficiary.Gender = beneficiary.gender
    _beneficiary.Birthday = beneficiary.birthday
    _beneficiary.IdEmployee = beneficiary.idEmployee

    db.commit()
    db.refresh(_beneficiary)
    return _beneficiary


def delete(db: Session, beneficiaryId: int):
    _beneficiary = get_id(db, beneficiaryId)
    db.delete(_beneficiary)
    db.commit()
