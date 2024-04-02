# encoding='utf-8
# @Time: 2024-03-13
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests


def get_proxy():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }
    params = {
        'neek': '321a408a',
        'num': '400',
        'type': '2',
        'time': '4',
        'pro': '0',
        'city': '0',
        'yys': '0',
        'port': '1',
        'pack': '0',
        'ts': '0',
        'ys': '0',
        'cs': '0',
        'lb': '1',
        'sb': '',
        'pb': '4',
        'mr': '1',
        'regions': '',
    }
    response = requests.get('http://webapi.http.zhimacangku.com/getip',
                            params=params, headers=headers, verify=False)
    if response.json()['code'] == 0:
        proxys = response.json()['data']
    proxies = [{"http": "http://" + item['ip'] +
                ":" + str(item['port']), "https": "http://" + item['ip'] +
                ":" + str(item['port'])} for item in proxys]
    # ic(proxies)
    #
    # ic(proxys)
    return proxies


def request_test(proxie):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Ps-Dataurlconfigqid': '0xaa8cec6f0005a0d5',
        'Referer': 'https://www.baidu.com/s?wd=fdafda',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'is_referer': 'https://www.baidu.com/',
        'is_xhr': '1',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'ie': 'utf-8',
        'newi': '1',
        'mod': '1',
        'isid': '1D080C3442641732',
        'wd': 'fdafda',
        'rsv_sid': '40171_40206_40212_40223_40294_40291_40288_40284_40317_40079_40365_40351_40298_40366_40376_40403_40416',
        '_ss': '1',
        'clist': '',
        'hsug': '',
        'f4s': '1',
        'csor': '6',
        '_cr1': '13668',
    }

    response = requests.get('https://www.baidu.com/s',
                            params=params, proxies= proxie , headers=headers).text
    ic(response)


# if __name__ == '__main__':
#     get_proxy()
#     # request_test(get_proxy()[0])
#
