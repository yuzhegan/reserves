# encoding='utf-8

# @Time: 2024-04-02
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests


class OzonApi:
    def __init__(self):
        self.url = 'https://seller.ozon.ru/api/site/seller-analytics/what_to_sell/data/v3'
        self.headers = {
            "authority": "www.ozon.ru",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "referer": "https://www.ozon.ru/",
            "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        self.client_id = '1654428'
        self.api_key = ''
        self.headers['x-o3-app-name'] = 'seller-ui'
        self.headers['x-o3-company-id'] = self.client_id
        self.headers['x-o3-language'] = 'zh-Hans'
        self.data = {
            'filter': {
                'stock': 'any_stock',
                'sku': '775079743',
            },
            'sort': {
                'key': 'sum_rating',
            },
            'limit': '50',
            'offset': '0',
        }

    def get_data(self):
        response = requests.post(
            self.url, headers=self.headers, json=self.data)
        # ic(response.text)
        ic(response.status_code)
        ic(response.json())
        return response.json()


if __name__ == '__main__':
    ozon = OzonApi()
    ozon.get_data()
