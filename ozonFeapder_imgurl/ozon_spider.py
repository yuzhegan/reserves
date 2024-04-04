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
from feapder import Item, UpdateItem 
from parseData import parseData
import random
import polars as pl
from cookie_pool import GenCookie
from read_file import ReadFile


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

    # 这种方式获取的cookies 需要科学
    file_path = './ozonFeapder_imgurl/data.xlsx'
    rd = ReadFile(file_path)
    df = rd.df
    ws = rd.ws


    def start_requests(self):
        gencookies = GenCookie()  # 实例化可以更换各个地方的cookie
        self.cookies, self.ua, self.headers = gencookies.gen_cookie()
        for index, row in self.df.iterrows():
            url = row['商品链接']
            yield feapder.Request(url = url,
                                  method="GET",
                                  headers=self.headers,
                                  download_midware=self.download_midware2,
                                  callback=self.parse_list,
                                  meta = {
                                      # 'index': index,
                                      'row': row.to_dict()
                                  }
                                  )

    def download_midware2(self, request):
        url = request.url
        response = self.session.get(url, 
                                    headers=self.headers, impersonate=self.ua,
                                    cookies=self.cookies,
                                    timeout=30)
        # with open('ozonfeapder.html', 'w') as f:
        #     f.write(response.text)

        return request, response

    def parse_list(self, request, response):
        row = request.meta['row']
        html = etree.HTML(response.text)
        data = html.xpath('//link[@rel="preload"]/@href')
        if not data:
            data = html.xpath('//div[@class="rj"]/img/@src')
            if not data:
                data = html.xpath('//div[@class="jn6 j6n"]//img/@src')
        imgurl = data[0] if data else ''
        item = Item()
        item['图片连接'] = imgurl
        for k, v in row.items():
            item[k] = v
        yield item



if __name__ == "__main__":
    OzonSpider(redis_key="ozon:OzonSpider").start()
