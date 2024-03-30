# -*- coding: utf-8 -*-
"""
Created on 2024-01-13 11:27:56
---------
@summary:
---------
@author: dav
"""

import feapder
from curl_cffi import requests
import time
from lxml import etree
import json
from feapder import Item
from parseData import parseData
import random
import polars as pl
from cookie_pool import GenCookie


class OzonSpider(feapder.Spider):
    # 自定义数据库，若项目中有setting.py文件，此自定义可删除
    # __custom_setting__ = dict(
    #     REDISDB_IP_PORTS="192.168.0.106:6379", REDISDB_USER_PASS="", REDISDB_DB=0
    # )
    session = requests.Session()
    headers = {
        'authority': 'www.ozon.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    str_today = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 这种方式获取的cookies 需要科学

    df = pl.read_excel('./ozonFeapder/客户搜素词.xlsx')
    df = df.filter(pl.col('openOff') == 'on')
    search_text_list = df.drop_nulls()['searchTerm'].to_list()
    print(len(search_text_list))

    def start_requests(self):
        gencookies = GenCookie()  # 实例化可以更换各个地方的cookie
        self.cookies, self.ua, self.headers = gencookies.gen_cookie()
        # self.cookies = gencookies.ChangeAddress(self.cookies,'54.677666','39.572836' )
        self.cookies = gencookies.ChangeAddress(self.cookies, self.ua, self.headers,'54.483441','36.218069' )
        yield feapder.Request('https://www.ozon.ru/',
                              method="GET",
                              headers=self.headers,
                              # use_session=True,
                              # download_midware=self.download_midware1,
                              )


    def parse(self, request, response):
        # print(response.cookies)
        # cookies = response.cookies
        # search_text_list = ['шик волосогон от засоров']
        print(self.cookies)
        for search_text in self.search_text_list:
            print(search_text)
            for page in range(1, 2):
                # time.sleep(random.randint(2, 4))
                params = {
                    'category_was_predicted': 'true',
                    'deny_category_prediction': 'true',
                    'from_global': 'true',
                    'page': page,
                    'text': search_text,
                    # 'tf_state': 'e3EYXzH7HAcMY9i_BLVlQFgptMXaYbH2X5vUE_LZLbdeYKCP',
                }

                yield feapder.Request('https://www.ozon.ru/search/',
                                      method="GET",
                                      headers=self.headers,
                                      # use_session=True,
                                      params=params,
                                      download_midware=self.download_midware2,
                                      callback=self.parse_list,
                                      )

    def download_midware2(self, request):
        response = self.session.get('https://www.ozon.ru/search/', params=request.params,
                                    headers=self.headers, impersonate=self.ua,
                                    cookies=self.cookies,
                                    timeout=30)
        # with open('ozonfeapder.html', 'w') as f:
        #     f.write(response.text)

        return request, response

    def parse_list(self, request, response):
        # with open('ozonfeapder.html', 'w') as f:
        #     f.write(response.text)
        html = etree.HTML(response.text)
        data = html.xpath(
            '//div[contains(@id,"state-searchResultsV2")]/@data-state')
        # print(len(data))
        # print(data)
        data = json.loads(data[0])
        # with open('ozonfeapder.json', 'w') as f:
        #     f.write(str(data))
        # items = data['items']
        # print(items[0])
        # parseData(data, request.params['text'], self.str_today, request.params['page'])
        datas = data['items']
        print(len(datas))
        count = 0
        for data in datas:
            count += 1
            item = Item()
            item.table_name = 'ozon'
            search_text = request.params['text']
            page = request.params['page']
            pdata = parseData(data, search_text, self.str_today, page, count)
            item.ImageUrl = pdata[0]
            item.skuId = pdata[1]
            item.title = pdata[2]
            item.url = pdata[3]
            item.price = pdata[4]
            item.rating = pdata[5]
            item.review = pdata[6]
            item.MaxAddToCart = pdata[7]
            item.search_text = pdata[8]
            item.search_text = pdata[9]
            item.pageRank = pdata[10]
            item.Advert = pdata[11]
            item.page = pdata[12]
            item.rank = pdata[13]
            item.deliveyTime = pdata[14]
            yield item


if __name__ == "__main__":
    OzonSpider(redis_key="ozon:OzonSpider").start()
