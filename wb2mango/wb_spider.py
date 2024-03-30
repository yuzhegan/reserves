# -*- coding: utf-8 -*-
"""
Created on 2024-01-12 11:39:05
---------
@summary:
---------
@author: dav
"""
import feapder
import time
from address import GenAddressDest
import json
from feapder import Item
import execjs
from utils import *
from Parsewb import Pasewb
import polars as pl


class WbSpider(feapder.Spider):
    # 自定义数据库，若项目中有setting.py文件，此自定义可删除
    __custom_setting__ = dict(
        REDISDB_IP_PORTS="192.168.174.1:6379", REDISDB_USER_PASS="", REDISDB_DB=0
    )
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.ru',
        'Pragma': 'no-cache',
        'Referer': 'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%BA%D0%BE%D1%81%D0%BC%D0%B5%D1%82%D0%B8%D0%BA%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D0%BF%D0%BE%D0%B4%D1%80%D0%BE%D1%81%D1%82%D0%BA%D0%BE%D0%B2',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    str_today = time.strftime("%Y-%m-%d", time.localtime())
    # print("params", params)

    def start_requests(self):
        df = pl.read_excel('./wb2mango/新wb中央仓库.xlsx')
        search_text = 'косметика для подростков'  # 搜索关键词
        for i in range(0, len(df)):  #切换地址
            dizhi = df['地址'][i]
            latitude = df['latitude'][i]
            longitude = df['longitude'][i]
            address = GenAddressDest(
                dizhi, latitude, longitude)
            # address = GenAddressDest(
            #     'Астана, шоссе Алаш, д. 69/1', '51.216201', '71.509418')
            dest, spp = address.get_address()
            for page in range(1, 8):   #切换页数
                params = {
                    'TestGroup': 'no_test',
                    'TestID': 'no_test',
                    'appType': '1',
                    'curr': 'rub',
                    'dest': str(dest),
                    'page': str(page),
                    'query': search_text,
                    'resultset': 'catalog',
                    'sort': 'popular',
                    'spp': spp,
                    'suppressSpellcheck': 'false',
                }
                # for page in range(1, 8):
                print("开始请求数据。。。。。。。。")
                yield feapder.Request("https://search.wb.ru/exactmatch/ru/common/v4/search",
                                      method="GET",
                                      headers=self.headers,
                                      params=params,
                                      page=page,
                                      search_text=search_text,
                                      callback=Pasewb.parse,
                                      )   # callback为回调函数,如果放到前面可能会报错

    def parse(self, request, response):
        print("解析数据中。。。。。。。。")
        # response.enconding="utf-8"
        response.encoding_errors = 'strict'
        # 提取数据
        datas = response.json['data']['products']
        print(f"datas有{len(datas)}条数据")
        search_text = request.search_text
        page = request.page
        # pasewb = Pasewb(datas=datas, search_text=search_text, page=page)
        # pasewb.parse()
        for data in datas:
            item = Item()
            item.table_name = "wbmongo"
            time1 = data["time1"]
            time2 = data["time2"]
            skuid = str(data["id"])
            url = 'https://www.wildberries.ru/catalog/{}/detail.aspx'.format(skuid)
            Imageurl = GetImageurl(skuid)
            root = data["root"]
            brand = data["brand"]
            brandId = data["brandId"]
            siteBrandId = data["siteBrandId"]
            # colors = str(data["colors"])
            name = data["name"]
            supplier = data["supplier"]
            supplierId = data["supplierId"]
            supplierRating = data["supplierRating"]
            priceU = int(data["priceU"])/100
            salePriceU = int(data["salePriceU"])/100
            sale = int(data["sale"])
            logisticsCost = int(data["logisticsCost"])/100
            returnCost = int(data["returnCost"])/100
            pics = data["pics"]
            rating = data["rating"]
            reviewRating = data["reviewRating"]
            feedbacks = data["feedbacks"]
            adcpm = AdPormotion(data,"cpm")
            adpromotion = AdPormotion(data,"promotion")
            adpromoPosition = AdPormotion(data,"promoPosition")
            adposition = AdPormotion(data,"position")
            adadvertId = AdPormotion(data,"advertId")
            devileveyDay = GetdevileveyDay(time1, time2)
            search_text = search_text
            searchDate = self.str_today
            pageRank = 'Pg_' + str(page) + '_' + str(datas.index(data) + 1)
            page = page
            rank = datas.index(data) + 1
            item.skuid = skuid
            item.url = url
            item.Imageurl = Imageurl
            item.root = root
            item.brand = brand
            item.brandId = brandId
            item.siteBrandId = siteBrandId
            # item.colors = colors
            item.name = name
            item.supplier = supplier
            item.supplierId = supplierId
            item.supplierRating = supplierRating
            item.priceU = priceU
            item.salePriceU = salePriceU
            item.sale = sale
            item.logisticsCost = logisticsCost
            item.returnCost = returnCost
            item.pics = pics
            item.rating = rating
            item.reviewRating = reviewRating
            item.feedbacks = feedbacks
            item.adcpm = adcpm
            item.adpromotion = adpromotion
            item.adpromoPosition = adpromoPosition
            item.adposition = adposition
            item.adadvertId = adadvertId
            item.devileveyDay = devileveyDay
            item.search_text = search_text
            item.searchDate = searchDate
            item.pageRank = pageRank
            item.page = page
            item.rank = rank
            yield item



if __name__ == "__main__":
    WbSpider(redis_key="test1:test").start()
