# encoding='utf-8

# @Time: 2024-04-04
# @File: %
#!/usr/bin/env
from icecream import ic
import os

import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOiIxNmViMTk3NzlhOTE0YzY3OTFmNGEwNWVmY2I0ZTUyMCIsIlNlc3Npb25JZCI6ImQwYzM4NDY2Y2E4MzRmNjc5OWZmNTdlYTMzNGE0YTA3IiwiUGxhdGZvcm0iOiJPem9uIiwiaWF0IjoxNzEyMjI3MDkwLCJuYmYiOjE3MTIyMjcwOTAsImV4cCI6MTcxMjI1NTg5MCwiaXNzIjoiZ29sZGVicmlkZ2Vfc3VzZXIiLCJhdWQiOiJnb2xhZGJyaWRnZV9hdXNlciJ9.v5d1R8wI-WsR7r5hMd6YJFuY2H-R6sNhl7vQuH6pCDc',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://www.ozon.ru',
    'Pragma': 'no-cache',
    'Referer': 'https://www.ozon.ru/product/prozhektor-svetodiodnyy-ulichnyy-generica-50vt-chernyy-981698198/?asb=CQxCPW2HJ%252FJKRoLN3W76iedtvkmEMeB0cWw1IML533I%253D&asb2=pnq2HJlDEn9RklQi-zFITft8gEw4WWycr_rtUtpfHve_2uk0v-5shC1mHxTHUMQWAEkox2G9311doPH9mgqD7A&avtc=1&avte=2&avts=1712227168&keywords=%D0%9F%D1%80%D0%BE%D0%B6%D0%B5%D0%BA%D1%82%D0%BE%D1%80&sh=1ZurcM_0bw',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'skuids': '1233456827,467407375,1102273108',
    'culture': 'zh-CN',
}

response = requests.get('https://www.ozonabc.com/api/goods', params=params, headers=headers).json()
ic(response)
