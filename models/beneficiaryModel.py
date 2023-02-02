from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.manager import Base

class Beneficiary(Base):
    __tablename__="Beneficiary"
    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    FullName=Column(String)
    Relationship=Column(String)    
    Gender=Column(String)    
    Birthday=Column(DateTime)
    IdEmployee=Column(Integer, ForeignKey("Employee.id") )