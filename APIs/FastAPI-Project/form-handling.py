from fastapi import FastAPI, Form, UploadFile, File
from typing import Annotated, List

app = FastAPI()

@app.post("/login/")
async def login(
    username : Annotated[str, Form()],
    password : Annotated[str, Form()]
    ):
    return {
        "Username" : username,
        "Password" : password
    }


@app.post("/uploadfile/")
async def upload_file(file : Annotated[UploadFile, File()]):
    return {"File name": file}


@app.post("/savefile", content_type="multipart/form-data")
async def save_fild(files : Annotated[List[UploadFile], File(description="Upload multiple files")]):
    return {"Message" : [file.filename for file in files]}