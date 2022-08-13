from  sqlalchemy import Column, ForeignKey, Integer, String,Boolean ,Float 
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FilesExtensions(Base):
    __tablename__ = "filesextentions"
    id = Column(Integer, primary_key=True)
    file_name = Column(String, nullable=False)
    file_ext = Column(String, nullable=False)
    file_content = Column(String, nullable=False)
    