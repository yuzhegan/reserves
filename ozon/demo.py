# encoding='utf-8
# @Time: 2024-01-03
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests
import requests
session = requests.session()
import time

headers = {
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
cookies = {
    "cf_clearance": "XrUVdNF8RY20vu65YpvyBQiOYcH94PQXQEVtBlZoANk-1704262985-0-2-dbbf35b3.49bd9208.aa11de28-160.2.1704262985",
    "abt_data": "1eda7a85307db88c92164adebdf0d220:3b781ab8392dfb40f5e461025df9b39b52d867576650121eeaeab24b4e1e7e80ecb80effd658b1f94be050eb544952f6dc5a0046fdccb886b5a3793cb3e5faf196c53645e3951131a933e7a69ce60e8ca8bebb7c2c949428d38d6cf515ed2a3eade049659a347a58b183dadd8ac6742217b77637bd8b8314eb690148615dd67bd1d2d63ab4d7f98779461400e3030d98ca3bddb10f9253c93d833bac83b10273011fcd75d1ee6c5679207d24992764f5bf6630cbe1a6577ae17eb3787d4659df",
}

session.headers.update(headers)
url = "https://www.ozon.ru/"
response = session.post(url, cookies=cookies)
# print(response.text)
with open("demo.html", "w", encoding="utf-8") as f:
    f.write(response.text)

# print(response)
# time.sleep(1)
# response = session.get(url)
# print(response)
