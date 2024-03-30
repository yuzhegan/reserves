# encoding='utf-8

# @Time: 2023-09-30
# @File: %
#!/usr/bin/env
from icecream import ic
import os
from PIL import Image
from io import BytesIO

import ddddocr
import requests


class GeneralOcr():
    def __init__(self, slideImg, bgImg):
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://login.dangdang.com',
            'Pragma': 'no-cache',
            'Referer': 'https://login.dangdang.com/?returnurl=https%3A%2F%2Fwww.dangdang.com%2F',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.12',
            'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.sildeImg = self.WriteImg(slideImg, 61, 61, 'sildeImg')
        self.bgImg = self.WriteImg(bgImg, 350, 175, 'bgImg')
        det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

        with open('./dangdang/Img/sildeImg.png', 'rb') as f:
            self.target_bytes = f.read()

        with open('./dangdang/Img/bgImg.png', 'rb') as f:
            self.background_bytes = f.read()

        self.res = det.slide_match(self.target_bytes, self.background_bytes, simple_target=True)
        print(self.res)




    def WriteImg(self, url, wideth, height, name):
        res = requests.get(url, headers=self.headers)
        img = Image.open(BytesIO(res.content))
        img = img.resize((wideth, height))
        img.save('./dangdang/Img/'+name+'.png')

a = GeneralOcr('https://slide.ddimg.cn/2e297089ee2d44ee8aeba7df14424498.png', 'https://slide.ddimg.cn/71b34886bcc74345a45c23325c994dfb.jpg').res['target'][0]

