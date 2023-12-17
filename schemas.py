#Allows the creation of schemas for the app
from pydantic import BaseModel

class CourseSchema(BaseModel):
    title:str
    description:str
    category:str
    image:str
    start_date:str
    end_date:str
    
class UserSchema(BaseModel):
    name:str
    phone:str
    
class EnrollmentSchema(BaseModel):
    course_id: int
    name:str
    phone:str
    enrollment_date:str