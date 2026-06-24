from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

class User(BaseModel):
    name:str
    age:int = Field(..., gt=0, Le=120)
    
    @field_validator("name")
    def name_must_not_be_empty(cls, v):
        if not v:
            return ValueError("Name must not be Empty")
        return v
        



@app.post("/users/")
async def create_user(user:User):
    u = {"sended user" : user.name, "sended age" : user.age}
    return u