# encoding='utf-8
# @Time: 2024-01-09
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests
from ParsewbV3 import Pasewb, DataWriter
import time
from address import GenAddressDest 

class WbSpider:
    def __init__(self, dest, spp):

        self.headers = {
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
        self.dest = str(dest)
        self.spp = str(spp)

        self.session = requests.session()
        self.session.headers.update(self.headers)
    def get_data(self, page, search_text):
        params = {
            'TestGroup': 'no_test',
            'TestID': 'no_test',
            'appType': '1',
            'curr': 'rub',
            # 'dest': '-1257786',
            'dest': str(self.dest),
            'page': page,
            # 'query': 'косметика для подростков',
            'query': search_text,
            'resultset': 'catalog',
            'sort': 'popular',
            # 'spp': '27',
            'spp': self.spp,
            'suppressSpellcheck': 'false',
        }
        response = self.session.get('https://search.wb.ru/exactmatch/ru/common/v4/search', params=params).json()
        datas = response['data']['products']
        # with open ('wb_data.json', 'w', encoding='utf-8') as f:
        #     f.write(str(datas))
        return datas

if __name__ == '__main__':
    search_text = 'косметика для подростков'
    address = GenAddressDest('Астана, шоссе Алаш, д. 69/1', '51.216201', '71.509418')
    dest, spp = address.get_address()

    spider = WbSpider(dest, spp)
    writer = DataWriter("./wbdemo.csv")
    for page in range(1, 8):
        data = spider.get_data(page, search_text)
        ic(len(data))
        datas = Pasewb(data, writer, search_text, page).parse()


