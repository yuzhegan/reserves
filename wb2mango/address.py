# encoding='utf-8
# @Time: 2024-01-09
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests
import time
class GenAddressDest():
    def __init__(self, dizhi, latitude, longitude):
        self.headers = {
            'authority': 'user-geo-data.wildberries.ru',
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'origin': 'https://www.wildberries.ru',
            'pragma': 'no-cache',
            'referer': 'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%B4%D1%83%D1%85%D0%B8%20%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B5%20%D1%81%D0%BB%D0%B0%D0%B4%D0%BA%D0%B8%D0%B5',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.dizhi = dizhi
        self.latitude = latitude
        self.longitude = longitude



    def get_address(self):
        params = {
            'currency': 'RUB',
            # 'latitude': '51.216201', #纬度
            # 'longitude': '71.509418', #经度
            'latitude': self.latitude, #纬度
            'longitude': self.longitude, #经度
            # 'locale': 'kz',
            'address': self.dizhi,
            # 'address': 'Астана, шоссе Алаш, д. 69/1',
            # 'dt': '1704795638',
            'dt': str(int(time.time())),
        }
        response = self.session.get('https://user-geo-data.wildberries.ru/get-geo-info', params=params, ).json()
        dest = str(response['destinations'][3])
        spp = response['xinfo'].split('spp=')[1]
        ic(self.dizhi)
        ic(dest)
        ic(spp)
        # ic(response)
        return dest, spp

# if __name__ == '__main__':
    # address = GenAddressDest('Астана, шоссе Алаш, д. 69/1', '51.216201', '71.509418')
    # address.get_address()
#获取dest 地址信息


# ic| response: {'address': 'Астана, шоссе Алаш, д. 69/1',
#                'currency': 'RUB',
#                'destinations': [12358388, 12358412, -8593081, 82],
#                'dt': 1704795638,
#                'ip': '103.171.177.36',
#                'latitude': 51.216201,
#                'locale': 'kz',
#                'longitude': 71.509418,
#                'shard': 0,
#                'userDataSign': 'version=1&uid=0&spp=27&timestamp=1704800085&sign=8b92131082312a0ece
# 11661f31fe4229b37e6b804a468914d6a357da17faef24',
#                'xinfo': 'appType=1&curr=rub&dest=82&spp=27'}



