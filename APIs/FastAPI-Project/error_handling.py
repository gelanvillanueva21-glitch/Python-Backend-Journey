from fastapi import FastAPI, HTTPException, status

app = FastAPI()

items_in_shop = ["sword", "shield", "potion"]

@app.get("/items/{item_name}")
async def get_item(item_name : str):
    if item_name not in items_in_shop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No Item Found here"
        )
    return {"item": item_name, "status": "Available"}