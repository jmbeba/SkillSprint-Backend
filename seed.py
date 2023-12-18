from models import Course, Enrollment
import random
from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from utils import generate_start_date, generate_end_date

load_dotenv()

engine = create_engine(os.getenv('POSTGRES_URI'), echo=True)
Session = sessionmaker(bind=engine)

session = Session()

session.query(Enrollment).delete()
session.commit()
session.query(Course).delete()
session.commit()


fake = Faker()

course_prefixes = ['Introduction to', 'Advanced', 'Fundamentals of', 'Mastering', 'Principles of']
course_subjects = ['Business', 'Computer Science', 'Data Science', 'Engineering', 'Mathematics', 'Physics']
course_suffixes = ['101', '202', '303', 'Bootcamp', 'Workshop', 'Lab']




for _ in range(20):
    subject = random.choice(course_subjects)
    course_title = f"{random.choice(course_prefixes)} {subject} {random.choice(course_suffixes)}"
    
    description = [
        f"This course covers the fundamentals of {course_title}.",
        f"Explore the evolving landscape of {course_title}.",
        "Discover effective tools businesses use to thrive in the digital era."
    ]
    
    random.shuffle(description)
    
    new_course = Course(
        title=f"{random.choice(course_prefixes)} {subject} {random.choice(course_suffixes)}",
        description="".join(description),
        category=subject,
        image="https://images.unsplash.com/photo-1664575601711-67110e027b9b?q=80&w=1471&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        start_date=generate_start_date(),
        end_date=generate_end_date()
        )
    
    session.add(new_course)
    session.commit()
    
session.close()