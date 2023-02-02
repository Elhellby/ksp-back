from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: Optional[int]
    picture: str
    name: str
    position: str
    salary: int
    status: Optional[bool]=None
    creationDate: Optional[datetime]=None

    class Config:
        orm_mode: True

class RequestEmployee(BaseModel):
    parameter:Employee=Field(...)

