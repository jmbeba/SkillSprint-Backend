from fastapi import FastAPI, Depends, HTTPException, status, Response
from schemas import CourseSchema, EnrollmentSchema
from models import Course, User, Enrollment
from sqlalchemy.orm import Session, joinedload
from database import get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

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
    course = db.query(Course).options(joinedload(Course.students)).filter(course_id == Course.id).first()
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

@app.post('/enrollments')
def add_enrollment(enrollment: EnrollmentSchema, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == enrollment.phone).first()
    
    print(user)
    
    if user == None:
        user = User(name=enrollment.name, phone=enrollment.phone)
        db.add(user)
        db.commit()
        
        new_enrollment = Enrollment(enrollment_date=enrollment.enrollment_date, course_id=enrollment.course_id, user_id=user.id)
        
        db.add(new_enrollment)
        db.commit()
    else:
        enrollment_exists = db.query(Enrollment).filter(Enrollment.user_id == user.id , Enrollment.course_id == enrollment.course_id).first()
        print(enrollment_exists)
        
        if enrollment_exists == None:
            new_enrollment = Enrollment(enrollment_date=enrollment.enrollment_date, course_id=enrollment.course_id, user_id=user.id)
        
            db.add(new_enrollment)
            db.commit()
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Course already enrolled")
    
    return {
        "message":"Enrollment successful"
    }
    
@app.get('/users')
def get_users(db:Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.get('/users/{user_id}')
def get_user(user_id:int, db:Session = Depends(get_db)):
    user = db.query(User).options(joinedload(User.enrolled)).filter(User.id == user_id).first()
    return user