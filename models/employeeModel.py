from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database.manager import Base
from sqlalchemy.orm import relationship

class Employee(Base):
    __tablename__="Employee"
    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    Picture=Column(String)
    Name=Column(String)
    Position=Column(String)
    Salary=Column(Integer)
    Status=Column(Boolean)
    CreationDate=Column(DateTime)
    Beneficiary=relationship("Beneficiary", backref="owner" )
    