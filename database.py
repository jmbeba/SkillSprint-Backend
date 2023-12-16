from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

#Connect app to our postgres db
engine = create_engine(os.getenv('POSTGRES_URI'), echo=True)
Session = sessionmaker(bind=engine)

#Define method to get db
def get_db():
    db = Session()
    
    try:
        yield db
    finally:
        db.close()