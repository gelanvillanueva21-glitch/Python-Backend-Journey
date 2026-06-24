from fastapi import FastAPI

app = FastAPI()


@app.post("/items/")
def create_item(name: str, price: float):
    return {"name": name, "price": price}



@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return {"item_id" : item_id, "name" : name, "price" : price}



@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message" : f"Item {item_id} deleted successfully"}