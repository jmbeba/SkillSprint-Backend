from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {
        "message":"Welcome to my first apis"
    }
    
@app.get('/courses')
def courses():
    return []    
    
@app.post('/courses')
def create():
    return {
        "message":"Course created successfully"
    }
    
@app.patch('/courses/{course_id}')
def update_course(course_id:int):
    return {"message":f"Course {course_id} updated successfully"}

@app.delete('/courses/{course_id}')
def delete_course(course_id:int):
    return {"message":f"Course {course_id} deleted successfully"}