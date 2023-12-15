from fastapi import FastAPI, Depends, HTTPException, status, Response
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
def course(course_id:int, db:Session = Depends(get_db)):
    course = db.query(Course).filter(course_id == Course.id).first()
    return course    
    
#Post a course    
@app.post('/courses')
def create_course(course: CourseSchema, db: Session = Depends(get_db)):
    new_course = Course(**course.model_dump())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {
        "message":"Course created successfully",
        "course":new_course
    }
    
#Update a course    
@app.patch('/courses/{course_id}')
def update_course(course_id:int):
    return {"message":f"Course {course_id} updated successfully"}

#Delete a course
@app.delete('/courses/{course_id}')
def delete_course(course_id:int, db:Session = Depends(get_db)):
    delete_course = db.query(Course).filter(Course.id == course_id).first()
    
    if delete_course == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course {course_id} does not exist")
    else:
        db.delete(delete_course)
        db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)