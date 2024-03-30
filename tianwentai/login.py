# encoding='utf-8

# @Time: 2024-01-01
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import re

# gen code 

# gen wxuser
import requests
from urllib.parse import urlparse, parse_qs

# print(len('041zmRkl25JJEc4rZqol2GIoI04zmRks'))
# exit()


class WxUserLogin:
    def __init__(self, filepath):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Linux\""
        }
        self.path = filepath
        self.codes = []
    def genWxUser(self, code):
        url = "https://weather.121.com.cn/szqx/api/wx.do"
        params = {
            "client": "sztw",
            "code": code,
            "redirect_uri": "https://weather.121.com.cn/sztwt/#/gr"
        }
        response = requests.get(url, headers=self.headers, params=params)
        redirect_url = response.url
        wxuser = None
        if "wxuser" in redirect_url:
            # 解析URL
            parsed_url = urlparse(redirect_url)
            # 提取查询字符串
            query_params = parse_qs(parsed_url.query)
            # 获取'wxuser'参数的值
            wxuser = query_params.get('wxuser', [None])[0]
            print("wxuser", wxuser)
            return wxuser
        return wxuser

    def ReadCode(self):
        with open(self.path, 'r') as f:
            code = f.read().split('\n')[-2]
        return code
    # def WaitForCode(self):
    #     while True:
    #         WxUser = WxUser('./tianwentai/code.txt')
    #         code = WxUser.ReadCode()
    #         wxuser = WxUser.genWxUser(code)
    #         if wxuser:
    #             print(wxuser)
    #             break
    #     return wxuser


# if __name__ == '__main__':
#     while True:
#         WxUser = WxUser('./tianwentai/code.txt')
#         code = WxUser.ReadCode()
#         wxuser = WxUser.genWxUser(code)
#         if wxuser:
#             print(wxuser)
#             break
    # filepath = './tianwentai/code.txt'
    # wxuser = WxUser(filepath)
    # codes = wxuser.ReadCode()
    # print(codes)
    # wxuser.genWxUser()
    # print(wxuser.genWxUser())
    # print(wxuser.genWxUser())


