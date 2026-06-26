from fastapi import FastAPI, Path, Body
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

class Task(BaseModel):
    title : Annotated[str, Field(min_length=3, max_length=30)] = "Title"
    category : Annotated[str, Field(min_length=3)] = "Category"


class User(BaseModel):
    username : Annotated[str, Field(min_length=5, max_length=50, pattern=r'^[a-zA-Z0-9_.-]+$')]


@app.put("/tasks/{task_id}")
async def getInfo(
    task_id: Annotated[int, Path(ge=1)], 
    task : Task,
    user : User,
    priority_score : Annotated[int, Body(ge=1, le=1000)] = 1
    ):
    return {
        "Id" : task_id,
        "Task" : [task.title, task.category],
        "Username" : user.username,
        "Priority" : priority_score
    }