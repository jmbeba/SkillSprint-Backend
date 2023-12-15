from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Connect app to our postgres db
engine = create_engine('postgres://admin:8LXeXhtgTWaFJI657fyUD0quR63qmGkD@dpg-clu8d27qd2ns73a92h70-a.frankfurt-postgres.render.com/courses_44lu')
Session = sessionmaker(bind=engine)

#Define method to get db
def get_db():
    db = Session()
    
    try:
        yield db
    finally:
        db.close()