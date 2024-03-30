# encoding='utf-8

# @Time: 2023-11-15
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import random
import requests
import re
from Proxy_JiGuang import Proxy_JiGuang


def GenJdIps():
    proxy = Proxy_JiGuang()
    proxy.SetLocalIp2WhiteList()
    ips = proxy.GenJG_Proxy_IPs()
    ic(ips)
    return ips


ips = GenJdIps()
ip = random.choice(ips)
proxies = {
    "http": "http://" + str(ip['outip'])+':'+str(ip['port']),
    "https": "https://" + str(ip['outip'])+':'+str(ip['port']),
}
ic(proxies)

headers = {
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


def GenLoaclIp(proxies):
    r = requests.get("http://txt.go.sohu.com/ip/soip", headers=headers, proxies=proxies)
    ip = re.findall(r'\d+\.\d+\.\d+\.\d+', r.text)[0]
    ic(ip)
    return ip


GenLoaclIp(proxies)
