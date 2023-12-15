from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, VARCHAR, DateTime, TIMESTAMP

#Create a base model
Base = declarative_base()

#Defining the Course model
class Course(Base):
    __tablename__ = 'courses'
    
    #Column definitions
    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    description = Column(VARCHAR, nullable=False)
    category = Column(String(), nullable=False)
    start_date = Column(DateTime(), nullable=False)
    end_date = Column(DateTime(), nullable=False)
    
    created_at = Column(TIMESTAMP)