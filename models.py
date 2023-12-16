from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, VARCHAR, DateTime, TIMESTAMP

#Create a base model
Base = declarative_base()

#Defining the Course model
class Course(Base):
    __tablename__ = 'courses'
    
    #Column definitions
    id = Column(Integer(), primary_key=True)
    title = Column(Text(), nullable=False)
    description = Column(VARCHAR, nullable=False)
    category = Column(Text(), nullable=False)
    start_date = Column(DateTime(), nullable=False)
    end_date = Column(DateTime(), nullable=False)
    
    created_at = Column(TIMESTAMP)
    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer(), primary_key=True)
    name = Column(Text(), nullable=False)
    phone = Column(VARCHAR, nullable=False, unique=True)