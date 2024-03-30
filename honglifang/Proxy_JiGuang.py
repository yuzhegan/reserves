# encoding='utf-8
# @Time: 2023-11-04
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests
import re
import random
# https://www.jghttp.com/api/new_api.html


class Proxy_JiGuang:
    def __init__(self):
        self.headers = {
            'Accept': 'text/html, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            # 'Origin': 'https://www.jghttp.com',
            'Pragma': 'no-cache',
            # 'Referer': 'https://www.jghttp.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'session-id': 'm7qafevl4ttau6uabu0vlump55',
        }
        # self.GenLoaclIp()
        # self.SetLocalIp2WhiteList()
        # self.GenJG_Proxy_IPs()
        # self.Test_ProxyIp(self.GenJG_Proxy_IPs())

    def GenLoaclIp(self):
        r = requests.get("http://txt.go.sohu.com/ip/soip")
        ip = re.findall(r'\d+\.\d+\.\d+\.\d+', r.text)[0]
        # ic(ip)
        return ip

    def SetLocalIp2WhiteList(self):
        params = (
            ('neek', '56779'),
            ('appkey', '9874820df44e114295aee48cb3ed6346'),
            ('white', self.GenLoaclIp()),
        )
        response = requests.get(
            'https://webapi.jghttp.alicloudecs.com/index/index/save_white', headers=self.headers, params=params).json()
        ic(response)

    def GenJG_Proxy_IPs(self):
        params = (
            ('num', '100'),
            ('type', '2'),
            ('pro', '440000'),
            ('city', '440500'),
            ('yys', '0'),
            ('port', '1'),
            ('time', '7'),
            ('ts', '0'),
            ('ys', '0'),
            ('cs', '0'),
            ('lb', '1'),
            ('sb', '0'),
            ('pb', '4'),
            ('mr', '1'),
            ('regions', ''),
        )

        response = requests.get('http://sd.jghttp.alicloudecs.com/get_ip',
                                headers=self.headers, params=params, verify=False).json()
        ips = response['data']
        # ic(ips)
        # ip = random.choice(ips)
        # proxies = {
        #     'http': 'http://' + str(ip['ip'])+':'+str(ip['port']),
        #     'https': 'https://' + str(ip['ip'])+':'+str(ip['port']),
        # }
        # ic(proxies)
        # random to choose from ips
        # print(ips)
        # ic(response)
        return ips

    def Test_ProxyIp(self, proxies):
        response = requests.get(
            'http://httpbin.org/ip', headers=self.headers, proxies=proxies, verify=False).json()
        ic(response)
# if __name__ == '__main__':
#     dd = Proxy_JiGuang()
