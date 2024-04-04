# encoding='utf-8

# @Time: 2023-12-30
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import csv
import html
from feapder import Item

def htmlEncode(s):
    return html.unescape(s)

def parseData( item, search_text, search_date, page, count):
    # writer = DataWriter('data.csv')
    # for item in items:
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
    try:
        deliveyTime = item['multiButton']['ozonButton']['addToCartButtonWithQuantity']['text']
    except:
        deliveyTime = ""

    skuId = item['skuId']
    try:
        ImagUrl = item['tileImage']['items'][0]['image']['link']
    except:
        ImagUrl = item['tileImage']['items'][1]['image']['link']

    pageRank = "Pg" + str(page) + "_" + str(count)
    # 判断是否是广告
    if 'advert' in url.lower():
        Advert = 'True'
    else:
        Advert = 'False'
    # htmlEncode
    title = htmlEncode(title)

    data = [ImagUrl, skuId, str(title), url,
            str(price), str(rating), str(review), str(MaxAddToCart), search_text, search_date, pageRank, Advert, page, count, deliveyTime]
    # print(data)


    return data

