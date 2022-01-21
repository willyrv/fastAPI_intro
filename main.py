# main.py

from re import L
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/version")
async def get_version():
    return {"version": "0.0.1"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

## Don't forget to put fixed paths first

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the ID of the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Otherwise /users/me would be interpreted as /users/user_id="me"


## Using pydantic to Declare JSON Data Models (Data Shapes)

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict



