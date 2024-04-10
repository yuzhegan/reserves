# encoding='utf-8

# @Time: 2024-04-09
# @File: %
#!/usr/bin/env

from icecream import ic
import os
from pydantic import BaseModel
from pymongo import MongoClient
from typing import Union
import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder  # 导入jsonable_encoder来处理MongoDB文档
from bson import ObjectId


app = FastAPI()
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["ozon"]
collection_category = db['ozon_category']  # 类目数据
collection_product = db['ozon_product']  # 详情数据

def convert_query(query):
    converted_query = {}
    for key, value in query.items():
        if isinstance(value, dict):
            converted_value = {}
            if 'max' in value:
                converted_value['$lt'] = value['max']
            if 'min' in value:
                converted_value['$gte'] = value['min']
            converted_query[key] = converted_value
        else:
            converted_query[key] = value
    return converted_query


class Category(BaseModel):
    label: list
    formdata: dict
    roa: dict
    page: int = 1  # 这里应该是类属性，不是字典的一部分

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/category/")
async def create_category_list(category: Category):
    category_dict = category.dict()  # 将模型转换为字典
    page = category.page
    per_page = 50
    skip = (page - 1) * per_page
    limit = per_page
    formdata = category_dict['formdata']
    ic(formdata)
    # 转化为MongoDB查询语句
    serializable_result = []
    if len(category.label) == 0:
        return "No label"
    elif len(category.label) == 1:
        # 一级类目
        category1 = category.label[0]
        query = {
            "一级级分类": category1,  # 假设这里使用传入的类别
        }
    elif len(category.label) == 2:
        category1 = category.label[0]
        category2 = category.label[1]
        query = {
            "一级分类": category1,
            "二级分类": category2
                }
    elif len(category.label) == 3:
        category1 = category.label[0]
        category2 = category.label[1]
        category3 = category.label[2]
        query = {
            "一级分类": category1,
            "二级分类": category2,
            "三级分类": category3
        }

    query.update(formdata)
    query = convert_query(query)
    ic(query)
    result = collection_category.find(query).skip(skip).limit(limit)
    
    # 将MongoDB文档转换为可序列化的格式
    for doc in result:
        doc['_id'] = str(doc['_id'])  # 将ObjectId转换为字符串
        serializable_result.append(doc)
    return serializable_result


@app.post("/Product/")
async def create_category_list(product: Category):
    product_dict = product.dict()  # 将模型转换为字典
    page = product.page
    per_page = 50
    skip = (page - 1) * per_page
    limit = per_page
    formdata = product_dict['formdata']
    for key, value in formdata.items():
        for k, v in value.items():
            if "min" in k:
                formdata[key] = {"$gte": v}
            elif "max" in k:
                formdata[key] = {"$lte": v}
    
    if len(product.label) == 0:
        return "No label"
    elif len(product.label) == 1:
        # 一级类目
        category1 = product.label[0]

        query = {
            "一级分类": category1,  # 假设这里使用传入的类别
        }
    elif len(product.label) == 2:
        category1 = product.label[0]
        category2 = product.label[1]
        query = {
            "一级分类": category1,
            "二级分类": category2
        }
    elif len(product.label) == 3:
        category1 = product.label[0]
        category2 = product.label[1]
        category3 = product.label[2]
        query = {
            "一级分类": category1,
            "二级分类": category2,
            "三级分类": category3
        }
    elif len(product.label) == 4:
        category1 = product.label[0]
        category2 = product.label[1]
        category3 = product.label[2]
        category4 = product.label[3]
        query = {
            "一级分类": category1,
            "二级分类": category2,
            "三级分类": category3,
            "四级分类": category4
        }

    query.update(formdata)
    ic(query)
    result = collection_product.find(query).skip(skip).limit(limit)
    
    # 将MongoDB文档转换为可序列化的格式
    serializable_result = []
    for doc in result:
        doc['_id'] = str(doc['_id'])  # 将ObjectId转换为字符串
        serializable_result.append(doc)
        
        return serializable_result


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, port=5050, host="0.0.0.0")
