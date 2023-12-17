from database import get_db
from models import Enrollment
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.getenv('POSTGRES_URI'), echo=True)
Session = sessionmaker(bind=engine)

session = Session()

print(session.query(Enrollment).all())

session.close()