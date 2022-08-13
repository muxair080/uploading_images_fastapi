from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# DATABASE_NAME = "HospitalProject.db"
# DATABASE_URL = f'sqlite:///{DATABASE_NAME}'
DATABASE_URL = 'postgresql://postgres:uzair@localhost/file_managing'

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
