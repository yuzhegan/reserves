# encoding='utf-8

# @Time: 2023-10-03
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests
import execjs



class taobao_login():
    def __init__(self) -> None:

        self.session = requests.session()

        self.headers = {
            'authority': 'login.taobao.com',
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
        self.session.headers.update(self.headers)
        self.GetCookie()  # 获取cookie
        self.passwd2 = self.GetPasswd2('123456')  # 获取加密后的密码
        ic(self.passwd2)

    def GetCookie(self):
        # add headers to session
        response = self.session.get('https://login.taobao.com/')
        ic(response.cookies.get_dict())

    def GetPasswd2(self, passwd):
        with open ('./taobao/demo.js', 'r') as f:
            js = f.read()
        ctx = execjs.compile(js)
        return ctx.call('getpwd', passwd)

if __name__ == '__main__':
    login = taobao_login()

