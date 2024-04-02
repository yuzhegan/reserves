# encoding='utf-8

# @Time: 2024-04-02
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests


class OzonApi:
    def __init__(self):
        self.url = 'https://api-seller.ozon.ru/v1/analytics/data'
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
        self.api_key = '316033f2-f1c3-4a9e-a61c-6268f8c5b4a5'
        self.client_id = '1654428'
        self.headers['Client-Id'] = self.client_id
        self.headers['Api-Key'] = self.api_key
        self.data = {
            "date_from": "2024-03-01",
            "date_to": "2024-03-31",
            "metrics": [
                "unknown_metric",
                "hits_view_search",
                "hits_view_pdp",
                "hits_view",
                "hits_tocart_search",
                "hits_tocart_pdp",
                "hits_tocart",
                "session_view_search",
                "session_view_pdp",
                "session_view",
                "conv_tocart_search"

            ],
            "dimension": [
                "sku",
                "day",
                "category3",
                "category4",
            ],
            "filters": [],
            "sort": [
                {
                    "key": "hits_view_search",
                    "order": "DESC"
                }
            ],
            "limit": 1000,
            "offset": 0
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
