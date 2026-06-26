from fastapi import FastAPI
from pydantic import  BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr


class UserOut(BaseModel):
    username: str
    email: EmailStr


@app.post("/register", response_model=UserOut)
async def register_user(user: UserIn):
    return user