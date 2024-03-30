# encoding='utf-8

# @Time: 2023-12-30
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import csv
from mogodb import insert_data_to_mongo

class DataWriter:
    def __init__(self, file_name):
        # 打开文件并保持打开状态
        self.file = open(file_name, 'w', encoding='utf-8')
        self.writer = csv.writer(self.file)
        # 写入标题
        header = ["ImagUrl", "skuId", "title", "url",
                  "price", "rating", "review", "MaxAddToCart", "SearchText", "SearchDate", "pageRank", "Advert", "page", "rank"]
        self.writer.writerow(header)

    def writeData(self, data):
        # 确保每个项目都是字符串
        # data_str = [str(item) for item in data]
        # 写入一行数据
        self.writer.writerow(data)
        # self.file.write(';'.join(data) + '\n')
        return

    def close(self):
        # 关闭文件
        self.file.close()
        return

import html

class ParseData:
    def __init__(self, data):
        self.data = data

    def htmlEncode(self, s):
        return html.unescape(s)


    def parseData(self, search_text, search_date, page):
        items = self.data['items']
        # writer = DataWriter('data.csv')
        count = 0
        for item in items:
            url = "https://www.ozon.ru" + item['action']['link']
            price = (item['mainState'][0]['atom']['priceV2']
                     ['price'][0]['text'].strip(' ₽'))
            try:
                title = item['mainState'][1]['atom']['textAtom']['text']
                # print(title)
            except:
                try:
                    title = item["mainState"][2]["atom"]["textAtom"]["text"]
                except:
                    title = item["mainState"][3]["atom"]["textAtom"]["text"]
            try:
                # rating = item['mainState'][2]['atom']['items'][0]['title'].strip()
                rating = item["mainState"][3]["atom"]["labelList"]["items"][0]["title"]
            except:
                try:
                    rating = item["mainState"][2]["atom"]["labelList"]["items"][0]["title"]
                    if 'b>' in rating:
                        rating = item["mainState"][4]["atom"]["labelList"]["items"][0]["title"]
                except:
                    try:
                        rating = item["mainState"][4]["atom"]["labelList"]["items"][0]["title"]
                    except:
                        rating = 0
            try:
                # review = (item['mainState'][2]['atom']['items']
                          # [1]['title'].strip(' отзывов'))
                review = item["mainState"][3]["atom"]["labelList"]["items"][1]["title"].replace(' отзыва', '').replace('отзывов', '').replace(' отзыв', '')
            except:
                try:
                    review = item["mainState"][2]["atom"]["labelList"]["items"][1]["title"].replace(' отзыва', '').replace('отзывов', '').replace(' отзыв', '')
                    if 'b>' in review:
                        review = item["mainState"][4]["atom"]["labelList"]["items"][1]["title"].replace(' отзыва', '').replace('отзывов', '').replace(' отзыв', '')
                except:
                    try:
                        review = item["mainState"][4]["atom"]["labelList"]["items"][1]["title"].replace(' отзыва', '').replace('отзывов', '').replace(' отзыв', '')
                    except:
                        review = 0
            try:
                MaxAddToCart = item['multiButton']['ozonButton']['addToCartButtonWithQuantity']['maxItems']
            except:
                MaxAddToCart = 0 
            skuId = item['skuId']
            try:
                ImagUrl = item['tileImage']['items'][0]['image']['link']
            except:
                ImagUrl = item['tileImage']['items'][1]['image']['link']

            count += 1
            pageRank = "Pg" + str(page) + "_" + str(count)
            # 判断是否是广告
            if 'advert' in url.lower():
                Advert = 'True'
            else:
                Advert = 'False'
            # htmlEncode
            title = self.htmlEncode(title)

            data = [ImagUrl, skuId, str(title), url,
                    str(price), str(rating), str(review), str(MaxAddToCart), search_text, search_date, pageRank, Advert, page, count]
            insert_data_to_mongo('ozon','ozon',data)

            # writer.writeData(data)
        # writer.close()

        return data
