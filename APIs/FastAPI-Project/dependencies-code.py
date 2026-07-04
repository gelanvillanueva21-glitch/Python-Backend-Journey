from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

async def get_secret_code(code):
    if code != "MyPasswordIsPizza223DontTellAnyonePlease":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return "MyPasswordIsPizza223DontTellAnyonePlease"

@app.get("/vault")
async def open_vault(code : Annotated[str, Depends(get_secret_code)]):
    return {"message" : f"Vault unlocked using {code}"}