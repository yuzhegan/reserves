# encoding='utf-8
# @Time: 2023-09-11
# @File: %
#!/usr/bin/env
import execjs
import time
from icecream import ic
import os
import requests
def GenAesSign(randomkey, requestId, Xpex=True):
    e = {
        # "t": 1694419158248,
        'ct': 'pc',
        'permanent_id': '20230911142218827323294417821307852',
        'requestId': '2309121134209570aHyOSj_0d64',
    }
    t = int(time.time()*1000)
    # t = 1694488266092
    if requestId:
        e["requestId"] = requestId
    e["t"] = t
    if Xpex:
        a = "ct=" + e["ct"] + "&" + "permanent_id=" + e["permanent_id"] + \
            "&" + "requestId=" + e["requestId"] + "&" + "t=" + str(e["t"])
    else:
        a = "ct=" + e["ct"] + "&" + "permanent_id=" + e["permanent_id"] + \
            "&" + "requestId=" + e["requestId"] + \
            "&situation=login&" + "t=" + str(e["t"])
    print(a)
    # config md5 function
    def md5(str):
        import hashlib
        m = hashlib.md5()
        m.update(str.encode('utf-8'))
        return m.hexdigest()
    a = md5(a)
    def GenSign(a):
        if randomkey:
            key = randomkey
        else:
            key = 'qClxgXRjgpshoVhN'
        iv = '0102030405060708'
        with open("./dangdang/a.js", "r", encoding="utf-8") as f:
            js = f.read()
        ctx = execjs.compile(js)
        return ctx.call("GenAesString", a, key, iv)
    # print(GenSign(a))
    return GenSign(a), t
    # sign = GenSign(a)
def GetRandomkey(sign):
    headers = {
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
    data = {
        # 't': '1694423072381',
        'ct': 'pc',
        'permanent_id': '20230911142218827323294417821307852',
        'requestId': '2309111557244290NRtRvH_14ac',
    }
    data['sign'] = sign
    t = int(time.time()*1000)
    data['t'] = t
    response = requests.post(
        'https://login.dangdang.com/api/customer/loginapi/getRankey', headers=headers,  data=data).json()
    print(response)
    return [response['rankey'], response['requestId']]
def isShowSild(sign):
    headers = {
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
    data = {
      'ct': 'pc',
      'permanent_id': '20230911142218827323294417821307852',
      'requestId': '2309121134209570aHyOSj_0d64',
      # 'sign': 'yBeyPyLWRofOQOXWhQoOeldl2bXZ4Iam0ebgMKKKUJqqz/F0/2g7hiW6mZp3KHFY'
    }
    t = int(time.time()*1000)
    data['t'] = t
    response = requests.post('https://login.dangdang.com/api/customer/loginapi/isShowSlide', headers=headers, cookies=cookies, data=data).json()
    print(response)
def Genpic(t, sign):
    cookies = {
        'ddscreen': '2',
        'dest_area': 'country_id%3D9000%26province_id%3D111%26city_id%20%3D0%26district_id%3D0%26town_id%3D0',
        '__permanent_id': '20230911142218827323294417821307852',
        '__visit_id': '20230912103856807374974100056919463',
        '__out_refer': '',
        '__rpm': 'login_page...1694489655839%7Clogin_page...1694489669065',
        '__trace_id': '20230912113429155427497397496297370',
        'JSESSIONID': 'BE795EA71115ACA61834521ABD27FD13',
    }
    headers = {
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
    data = {
        # 't': '1694489669215',
        'ct': 'pc',
        'permanent_id': '20230911142218827323294417821307852',
        'requestId': '2309121134209570aHyOSj_0d64',
        'situation': 'login',
        # 'sign': 'C3vrAUozDZvZ80JKqMbwCxBDdm648kRUEu2p3AkZTZGNXV8Q+72UB6klJ2yS0CTj'
    }
    # t = int(time.time()*1000)
    data['t'] = t
    data['sign'] = sign
    response = requests.post('https://login.dangdang.com/api/customer/loginapi/getSlidingVerifyCode',
                             headers=headers, cookies=cookies, data=data).json()
    print(response)
if __name__ == "__main__":
    sign, t = GenAesSign('', '', True)
    print(sign)
    # randonkey, reqestid = GetRandomkey(sign)
    # sign = GenAesSign(randonkey, reqestid, False)
    # print(randonkey, reqestid)
    sign, t = GenAesSign('', '', False)
    print(sign, t)
    # sign = GenAesSign(randonkey, reqestid)
    # print(sign)
    Genpic(t, sign)
