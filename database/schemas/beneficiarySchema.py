from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class Beneficiary(BaseModel):
    id: Optional[int]
    fullName: str
    relationship: str
    gender: str
    birthday: datetime
    idEmployee: int

    class Config:
        orm_mode: True

class RequestBeneficiary(BaseModel):
    parameter: Beneficiary = Field(...)
