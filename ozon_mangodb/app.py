# encoding='utf-8

# @Time: 2024-04-09
# @File: %
#!/usr/bin/env
from icecream import ic
import os

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
