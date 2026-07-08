from fastapi import FastAPI, HTTPException, Depends, status
from typing import Annotated
from sqlalchemy.orm import Session
from schemas import get_database, UserAuth
from database import Base, engine
import auth


app = FastAPI()
app.include_router(auth.router)
Base.metadata.create_all(bind = engine)
db_dependency = Annotated[Session, Depends(get_database)]
user_dependency = Annotated[dict, Depends(auth.get_current_user)]


@app.get("/Login", status_code = status.HTTP_200_OK)
async def user(user : user_dependency, db : db_dependency):
    if not user:
        HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Authentication Failed"
        )
    return {"User" : user}


