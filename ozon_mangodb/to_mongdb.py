# encoding='utf-8

# @Time: 2024-04-10
# @File: %
#!/usr/bin/env
from icecream import ic
import os
from pymongo import MongoClient
import json
import pymongo
import polars as pl
import pandas as pd


db = MongoClient('mongodb://127.0.0.1:27017/')
mydb = db['ozon']
collection_category = mydb['ozon_category']
collection_product = mydb['ozon_product']

# df = pl.read_excel('./ozon_mangodb/ozon_test_output_pivot.xlsx')
#
# for row in df.rows():
#     data = {}
#     for i, col in enumerate(df.columns):
#         data[col] = row[i]
#     collection_category.insert_one(data)


df2 = pl.from_pandas(pd.read_excel('./ozon_mangodb/ozon_test_output.xlsx',
                                   ))


for row in df2.rows():
    data = {}
    for i, col in enumerate(df2.columns):
        data[col] = row[i]
    collection_product.insert_one(data)
