from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database = "postgresql://postgres:OjQ2REGdpgzS7BxrHTJF@ksp-database.cy4knequubpx.us-east-1.rds.amazonaws.com/postgres"

engine = create_engine(database)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()
