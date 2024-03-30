# encoding='utf-8

# @Time: 2023-12-30
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import csv
import html
from feapder import Item
from lxml import etree
import json
import feapder
import html
import time

class ParseData(feapder.Spider):
    # def __init__(self, data):
    #     self.data = data
    str_today = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    def htmlEncode(self, s):
        return html.unescape(s)
        

    def parse(self, request, response):
        print('parseData开始解析数据')
        search_text = request.params['text']
        search_date = self.str_today
        page = request.params['page']

        html = etree.HTML(response.text)
        data = html.xpath(
            '//div[contains(@id,"state-searchResultsV2")]/@data-state')
        # print(len(data))
        # print(data)
        data = json.loads(data[0])

        datas = self.data['items']
        # writer = DataWriter('data.csv')
        count = 0
        for data in datas:
            url = "https://www.ozon.ru" + data['action']['link']
            price = (data['mainState'][0]['atom']['priceV2']
                     ['price'][0]['text'].strip(' ₽'))
            try:
                title = data['mainState'][1]['atom']['textAtom']['text']
                # print(title)
            except:
                try:
                    title = data["mainState"][2]["atom"]["textAtom"]["text"]
                except:
                    title = data["mainState"][3]["atom"]["textAtom"]["text"]
            try:
                # rating = data['mainState'][2]['atom']['items'][0]['title'].strip()
                rating = data["mainState"][3]["atom"]["labelList"]["items"][0]["title"]
            except:
                try:
                    rating = data["mainState"][2]["atom"]["labelList"]["items"][0]["title"]
                    if 'b>' in rating:
                        rating = data["mainState"][4]["atom"]["labelList"]["items"][0]["title"]
                except:
                    try:
                        rating = data["mainState"][4]["atom"]["labelList"]["items"][0]["title"]
                    except:
                        rating = 0
            try:
                # review = (data['mainState'][2]['atom']['items']
                          # [1]['title'].strip(' отзывов'))
                review = data["mainState"][3]["atom"]["labelList"]["items"][1]["title"].replace(' отзыва', '').replace('отзывов', '').replace(' отзыв', '')
            except:
                try:
                    review = data["mainState"][2]["atom"]["labelList"]["items"][1]["title"].replace(' отзыва', '').replace('отзывов', '').replace(' отзыв', '')
                    if 'b>' in review:
                        review = data["mainState"][4]["atom"]["labelList"]["items"][1]["title"].replace(' отзыва', '').replace('отзывов', '').replace(' отзыв', '')
                except:
                    try:
                        review = data["mainState"][4]["atom"]["labelList"]["items"][1]["title"].replace(' отзыва', '').replace('отзывов', '').replace(' отзыв', '')
                    except:
                        review = 0
            try:
                MaxAddToCart = data['multiButton']['ozonButton']['addToCartButtonWithQuantity']['maxItems']
            except:
                MaxAddToCart = 0 
            skuId = data['skuId']
            try:
                ImagUrl = data['tileImage']['items'][0]['image']['link']
            except:
                ImagUrl = data['tileImage']['items'][1]['image']['link']

            count += 1
            pageRank = "Pg" + str(page) + "_" + str(count)
            # 判断是否是广告
            if 'advert' in url.lower():
                Advert = 'True'
            else:
                Advert = 'False'
            # htmlEncode
            title = self.htmlEncode(title)

            # data = [ImagUrl, skuId, str(title), url,
            #         str(price), str(rating), str(review), str(MaxAddToCart), search_text, search_date, pageRank, Advert, page, count]
            item = Item()
            item.table_name = 'ozonz'

            item.ImagUrl = ImagUrl
            item.skuId = skuId
            item.title = title
            item.url = url
            item.price = price
            item.rating = rating
            item.review = review
            item.MaxAddToCart = MaxAddToCart
            item.search_text = search_text
            item.search_date = search_date
            item.pageRank = pageRank
            item.Advert = Advert
            item.page = page
            item.rank = count
            yield item





