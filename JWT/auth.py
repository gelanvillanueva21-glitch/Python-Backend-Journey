from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal, Authentication
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from schemas import get_database, UserAuth

router = APIRouter(
    prefix = '/auth',
    tags = ['auth']
)


SECRET_KEY = '197b2c37c391bed93fe80344fe73b806947a65e36206e05a1a23c2fa12702fe3'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(
    schemes = ['bcrypt'],
    deprecated = 'auto'
)
oauth2_bearer = OAuth2PasswordBearer(tokenUrl = 'auth/token')
db_dependency = Annotated[Session, Depends(get_database)]

class Token(BaseModel):
    access_token : str
    token_type : str


@router.post("/", status_code = status.HTTP_201_CREATED)
async def create_user(
    users_data : UserAuth,
    db : db_dependency):
    
    new_user = Authentication(
        username = users_data.username,
        password = bcrypt_context.hash(users_data.password)
    )
    
    db.add(new_user)
    db.commit()


@router.post("/token", response_model = Token)
async def login_access(
    form_data : Annotated[OAuth2PasswordRequestForm, Depends()],
    db : db_dependency):
    
    user = auth_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = 'Could not Validate user'
        )
    token = create_access_token(user.username, user.id, timedelta(minutes = 20))
    return {
        "access_token": token, 
        "token_type": "bearer"
        }


def auth_user(username : str, password : str, db):
    
    user = db.query(Authentication).filter(Authentication.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False
    return user


def create_access_token(username : str, userId : int, expire_delta : timedelta):
    encode = {"sub" : username, "id" : userId}
    expires = datetime.utcnow() + expire_delta
    encode.update({"exp" : expires})
    return jwt.encode(encode, SECRET_KEY, algorithm = ALGORITHM)


async def get_current_user(token : Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms = ALGORITHM)
        username : str = payload.get("sub")
        user_id : int = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Could not Validate user"
            )
        return {
            "username" : username,
            "id" : user_id
            }
    except JWTError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Could not Validate user"
        )