# encoding='utf-8

# @Time: 2024-01-10
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import execjs
import time
from feapder import Item
import csv

# imageurl  搜索关键字basket-${t}.wbbasket.ru
# 送达日期  搜索关键字Доставка                завтра

class Pasewb(Item):
    def __init__(self, datas, search_text, page):
        # __unique_key__ = ["id", ""]
        self.datas = datas
        with open("./wb2mango/delievry.js", "r", encoding="utf-8") as f:
            self.js = f.read()
        self.ctx = execjs.compile(self.js)
        with open("./wb2mango/ImageUrl.js", "r", encoding="utf-8") as f:
            self.imgjs = f.read()
        self.imgctx = execjs.compile(self.imgjs)
        # self.writer = writer
        self.search_text = search_text
        self.str_today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.page = page
        print(self.str_today)



    def parse(self):
        print("开始写入")
        for data in self.datas:
            item = Item()
            item.table_name = "wbmongo"
            time1 = data["time1"]
            time2 = data["time2"]
            id = data["id"]
            url = 'https://www.wildberries.ru/catalog/{}/detail.aspx'.format(id)
            print(url)
            Imageurl = self.GetImageurl(id)
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
            adcpm = self.AdPormotion(data,"cpm")
            adpromotion = self.AdPormotion(data,"promotion")
            adpromoPosition = self.AdPormotion(data,"promoPosition")
            adposition = self.AdPormotion(data,"position")
            adadvertId = self.AdPormotion(data,"advertId")
            devileveyDay = self.GetdevileveyDay(time1, time2)
            search_text = self.search_text
            str_today = self.str_today
            pageRank = 'Pg_' + str(self.page) + '_' + str(self.datas.index(data) + 1)
            page = self.page
            rank = self.datas.index(data) + 1
            item.id = id
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
            item.adcpm = adcpm
            item.adpromotion = adpromotion
            item.adpromoPosition = adpromoPosition
            item.adposition = adposition
            item.adadvertId = adadvertId
            item.devileveyDay = devileveyDay
            item.search_text = search_text
            item.str_today = str_today
            item.pageRank = pageRank
            item.page = page
            item.rank = rank
            yield item
            print("写入成功")





    def AdPormotion(self, data, adpromotion):
        try:
            result = data["log"][adpromotion]
        except:
            result = ""
        return result
    def GetdevileveyDay(self, time1, time2):
        time = int(time1) + int(time2)  # 两个时间相加 然后调用js函数转化为到达时间
        # ic(self.ctx.call("deliveryDateTxt", time))
        return self.ctx.call("deliveryDateTxt", time)
    def GetImageurl(self, id):
        id = str(id)
        hosts = self.imgctx.call("constructHostV2", id)
        if len(id) == 9:
            imageurl = hosts + '/vol' + id[:4] +"/part" + id[:6] + "/" + id + '/images/c516x688/1.webp'
        elif len(id) == 8:
            imageurl = hosts + '/vol' + id[:3] +"/part" + id[:5] + "/" + id + '/images/c516x688/1.webp'
        elif len(id) == 7:
            imageurl = hosts + '/vol' + id[:2] +"/part" + id[:4] + "/" + id + '/images/c516x688/1.webp'

        return imageurl

# if __name__ == '__main__':
#     data = [
#         {
#             "time1": "130",
#             "time2": "6",
#             "id": "29054173",
#             "root": "1",
#             "brand": "1",
#             "brandId": "1",
#             "siteBrandId": "1",
#             "colors": ["1", "2", "3"],
#             "name": "1",
#             "supplier": "1",
#             "supplierId": "1",
#             "supplierRating": "1",
#             "priceU": "1",
#             "salePriceU": "1",
#             "sale": "1",
#             "logisticsCost": "1",
#             "returnCost": "1",
#             "pics": ["1", "2", "3"],
#             "log": {
#                 "cpm": "1",
#                 "promotion": "1",
#                 "promoPosition": "1",
#                 "position": "1",
#                 "advertId": "1"
#             }
#         }
#     ]
#     Pasewb(data).parse()
#
#
#
#
