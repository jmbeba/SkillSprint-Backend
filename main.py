from fastapi import FastAPI, Depends
from schemas import CourseSchema
from models import Course
from sqlalchemy.orm import Session
from database import get_db

app = FastAPI()

@app.get('/')
def index():
    return {
        "message":"Welcome to my first api"
    }
  
#Gets all courses    
@app.get('/courses')
def courses(db: Session = Depends(get_db)):
    events = db.query(Course).all()
    return events

#Get a single course
@app.get('/courses/{course_id}')
def course():
    return {}    
    
#Post a course    
@app.post('/courses')
def create_course(course: CourseSchema):
    print(course)
    return {
        "message":"Course created successfully"
    }
    
#Update a course    
@app.patch('/courses/{course_id}')
def update_course(course_id:int):
    return {"message":f"Course {course_id} updated successfully"}

#Delete a course
@app.delete('/courses/{course_id}')
def delete_course(course_id:int):
    return {"message":f"Course {course_id} deleted successfully"}