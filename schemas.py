#Allows the creation of schemas for the app
from pydantic import BaseModel

class Course(BaseModel):
    title:str
    description:str
    category:str
    start_date:str
    end_date:str