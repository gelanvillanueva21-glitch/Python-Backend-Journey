from pydantic import BaseModel, EmailStr, Field, field_validator, AfterValidator
from fastapi import FastAPI, Query
from typing import Annotated
import random

class User(BaseModel):
    username:str = Field(pattern=r'^[a-zA-Z0-9_.-]+$')
    email:EmailStr
    age:int = Field(gt=10)


    @field_validator('username')
    def username_must_not_contain_spaces(cls, v):
        if ' ' in v:
            raise ValueError('Username must not contain spaces')
        
        if 'admin' in v:
            raise ValueError('Username cannot be admin!')
        return v

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

@app.post("/register/")
async def register(user:User):
    return user


@app.get("/info/")
async def getInfo(password: Annotated[str | None, Query( min_length=3 ,max_length=50, pattern=r'^[a-zA-Z0-9_.-]+$')] = None):
    return {"Passwords" : password}


@app.get("/word/")
async def getWord(word: str | None = Query(min_length=3)):
    return {"Word" : word}


@app.get("/words/")
async def getWord(word: Annotated[str | None, Query(alias="Item-query", deprecated=True)] = None):
    return {"Word" : word}


@app.get("/hidden/")
def hiddenWord(word: Annotated[str | None, Query(include_in_schema=False)] = None):
    return {"Your Word" : word}


def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}