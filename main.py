from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/items/")
async def create_item(item: Item):
    print("create_item called..")
    print(item)
    return item
