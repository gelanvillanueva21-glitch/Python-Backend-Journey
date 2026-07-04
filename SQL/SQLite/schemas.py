from pydantic import BaseModel
from typing import Optional

class JobCreate(BaseModel):
    title : str
    company : str


class JobResponse(BaseModel):
    id : int
    title : str
    company : str
    is_active : Optional[bool] = True
    
    class Config:
        from_attributes = True