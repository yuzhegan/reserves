# encoding='utf-8
# @Time: 2024-01-05
# @File: %
#!/usr/bin/env
from icecream import ic
import os
from pymongo import MongoClient
client = MongoClient("mongodb://192.168.159.1:27017/")
def insert_data_to_mongo(db_name, collection_name, datas):
    """
    将数据插入MongoDB数据库的指定集合中。
    :param db_name: 数据库名称
    :param collection_name: 集合名称
    :param data: 要插入的数据，字典或字典列表
    """
    #重新构建数据
    data = {}
    data['ImagUrl'] = datas[0]
    data['skuId'] = datas[1]
    data['title'] = datas[2]
    data['url'] = datas[3]
    data['price'] = datas[4]
    data['rating'] = datas[5]
    data['review'] = datas[6]
    data['MaxAddToCart'] = datas[7]
    data['SearchText'] = datas[8]
    data['SearchDate'] = datas[9]
    data['pageRank'] = datas[10]
    data['Advert'] = datas[11]
    data['page'] = datas[12]
    data['Rank'] = datas[13]

    # 创建MongoDB客户端
    # 选择数据库
    db = client[db_name]
    # 选择集合
    collection = db[collection_name]
    # 插入数据
    if isinstance(data, list):
        # 如果data是列表，则插入多条数据
        collection.insert_many(data)
    else:
        # 插入单条数据
        collection.insert_one(data)
    # print("数据插入成功")
# 使用示例
# data = {"name": "张三", "age": 30}
# insert_data_to_mongo("mydatabase", "users", data)
