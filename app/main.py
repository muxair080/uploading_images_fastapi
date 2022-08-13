from fastapi import FastAPI, File, UploadFile, responses,Depends, HTTPException,status
from fastapi.responses import FileResponse
import uuid
import shutil,hashlib
from database import engine, get_db
from sqlalchemy.orm import Session
import os
import models,schema
app = FastAPI()

models.Base.metadata.create_all(bind= engine)

imgs_contents = []
file_path = '' 
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), db : Session = Depends(get_db)):
    imgs_ext = ['.jpg', '.jpeg', '.jpe' '.jif', '.jfif', '.jfi','.png','.gif','.webp','.tiff','.tif','.psd','.bmp','.dib','.heif','.heic','.ind','.indd','.indt', '.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2','.svg','.svgz','.ai']
    image_data = os.path.splitext(file.filename)
   
        
    contents = await file.read()
    hashed_content = hashlib.sha256(contents).hexdigest()
    images_query = db.query(models.FilesExtensions).filter(models.FilesExtensions.file_content == hashed_content).first()
    if not images_query:
        print(hashed_content)
        imgs_contents.append(hashed_content)
        print(imgs_contents)
        print(image_data[1])
        if(image_data[1] in imgs_ext):
            with open(f"StaticFolder\ {file.filename}",'wb') as image:
                shutil.copyfileobj(file.file, image)

                data = {"file_name" : image_data[0], "file_ext" : image_data[1], "file_content" : hashed_content}
                add_query = models.FilesExtensions(**data)
                db.add(add_query)
                db.commit()
                db.refresh(add_query)
        else:
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The given file is not image")

            # return {"File Error : " : "The given file is not image"}
    
        
    else:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER, detail="This image is already exists")
    
    return {"imge data : ":add_query}

@app.get('/image/{name}')
async def view(name : str):
    path = os.path.join(file_path, f"StaticFolder/{name}.png")
    print("path : ",path)
    if os.path.exists(path):
        return responses.FileResponse(path)
    return {"Message" : 'path dose not exist'}