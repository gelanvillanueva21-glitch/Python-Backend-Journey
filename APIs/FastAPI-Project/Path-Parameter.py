from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def getItemId(item_id : Annotated[int, Path(title="The id of the item", ge=1)]):
    return {"item Id" : item_id}