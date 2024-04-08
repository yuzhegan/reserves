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
    # 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOiJiZGFlMzZmMDkzMDg0ZWEwOTA0YjVjNDI0YTg5YTBmNiIsIlNlc3Npb25JZCI6IjdlOGQ2OTU3NTYzNTQxNzI5MTdmMDE3MmE5YmQxZjZiIiwiUGxhdGZvcm0iOiJPem9uIiwiaWF0IjoxNzEyMjQ0MTY2LCJuYmYiOjE3MTIyNDQxNjYsImV4cCI6MTcxMjI3Mjk2NiwiaXNzIjoiZ29sZGVicmlkZ2Vfc3VzZXIiLCJhdWQiOiJnb2xhZGJyaWRnZV9hdXNlciJ9.lSdspoIblarzFVpoJaZ2ctiiX_S5oaY5lg8w71SE0h8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive', 
    'Origin': 'https://www.ozon.ru',
    'Pragma': 'no-cache',
    'Referer': 'https://www.ozon.ru/product/otkryvashka-dlya-konservov-konservnyy-nozh-premium-631661610/?asb=hBooduaBh7Zkld%252FlcDCYf2dQQgRe4vd21PyuLjJSeO8%253D&asb2=fOQkh2NJAIWD5uA_wvZgdErVoBcPF82Eyq7H_Yw9H84EJQ0AoOOovUsGassvpiwajtnP_7RUcT2hsymruvVIpg&avtc=1&avte=2&avts=1712118106&keywords=%D0%9E%D1%82%D0%BA%D1%80%D1%8B%D0%B2%D0%B0%D0%BB%D0%BA%D0%B0&sh=UO8DFI8AuQ',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}
import base64
from io import BytesIO
from PIL import Image
import ddddocr


def GenerateCaptcha():
    response = requests.get('https://www.ozonabc.com/api/captcha', headers=headers).json()
    capchaId, captchadata =  response['data'][0]['id'], response['data'][0]['imgdata'].split(',')[1]
    print(capchaId, captchadata)
    captchadata = base64.b64decode(captchadata) # base64解码
    ocr = ddddocr.DdddOcr(beta=True)
    image = Image.open(BytesIO(captchadata))
    capchaCode = ocr.classification(image)
    print(capchaCode)

    # image.save('./captcha.png')
    return capchaId, capchaCode







def lanxiongLogin(capchaId, capchaCode):
    json_data = {
        'mobile': '19065486267',
        'password': 'Gyx.123456',
        'captcha': capchaCode,
        'captchaid': capchaId,
        'logintype': 1,
    }

    response = requests.post(
        'https://www.ozonabc.com/api/user/login', headers=headers, json=json_data).json()
    print(response['data'][0]['token'])
    return response['data'][0]['token']




def lanxiongGetGoods(token):

    headers['Authorization'] = f'Bearer {token}'
    params = {
        'skuids': '1158366011',
        'culture': 'zh-CN',
    }

    response = requests.get('https://www.ozonabc.com/api/goods',
                            params=params, headers=headers).json()
    ic(response)

if __name__ == '__main__':
    capchaId, capchaCode = GenerateCaptcha()
    token = lanxiongLogin(capchaId, capchaCode)
    lanxiongGetGoods(token)


