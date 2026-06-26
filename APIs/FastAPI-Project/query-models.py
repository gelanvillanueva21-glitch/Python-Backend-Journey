from typing import Annotated, Literal
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

class ProductFilter(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    order_by: Literal["price", "rating"] = "price"

@app.get("/products")
async def get_products(filters: Annotated[ProductFilter, Query()]):
    return {
        "limit_applied": filters.limit,
        "sorting_by": filters.order_by
    }