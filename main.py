from fastapi import FastAPI
from schemas import Course

app = FastAPI()

@app.get('/')
def index():
    return {
        "message":"Welcome to my first api"
    }
  
#Gets all courses    
@app.get('/courses')
def courses():
    return []

#Get a single course
@app.get('/courses/{course_id}')
def course():
    return {}    
    
#Post a course    
@app.post('/courses')
def create_course(course: Course):
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