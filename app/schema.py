from pydantic import BaseModel

class Files(BaseModel):
    file_name : str
    file_ext : str
    file_content : str

class FilesIn(Files):
    pass

class FilesOut(Files):
    id : int
    class Config:
        orm_mode  = True