from pydantic import BaseModel, Field
from typing import Annotated, Optional
from database import SessionLocal

class UserAuth(BaseModel):
    username : Annotated[str, Field(
        min_length = 5, 
        max_length = 30, 
        description = "Must atleast 5 characters and maximum of 30 characters")]
    password : Annotated[str, Field(
        min_length = 8,
        max_length = 50,
        description = "Must atleast 8 characters and maximum of 50 characters"
    )]



def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()