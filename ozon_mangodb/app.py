# encoding='utf-8

# @Time: 2024-04-09
# @File: %
#!/usr/bin/env
from icecream import ic
import os

from typing import Union
import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "good"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, port=5050)
