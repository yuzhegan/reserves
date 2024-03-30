# encoding='utf-8
# @Time: 2023-12-30
# @File: %
#!/usr/bin/env
from icecream import ic
import time
from curl_cffi import requests
from lxml import etree
import os
import json
from parseData import ParseData
from parseData import *
import re
from cookie_pool import GenCookie


class Ozon_Spider:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'authority': 'www.ozon.ru',
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

    def Get_cookies(self):
        response = self.session.get('https://www.ozon.ru/',
                                    impersonate="chrome110", headers=self.headers,  timeout=30,
                                    )
        response = self.session.get('https://www.ozon.ru/abt/result',
                                    impersonate="chrome110", headers=self.headers,  timeout=30,
                                    )
        # 这种方式获取的cookies 需要科学
        cookies = response.cookies
        ic(cookies)
        return cookies

    def ChangeAddress(self, cookies):
        # 换经纬度就可以切换地址了
        params = {
            'url': '/modal/commonDelivery?azimuth=0.504069202103&dt=1&lat=54.677666&long=39.572836&msid=030d9c7b-63a8-4442-b855-64d060c7abb1&neaf=f&nfr=t&pid=7&pv=2&pxlw=423.000000&src_main=%2Fsearch%2F%3Ffrom_global%3Dtrue%26text%3D%25D1%2588%25D0%25B8%25D0%25BA%2B%25D0%25B2%25D0%25BE%25D0%25BB%25D0%25BE%25D1%2581%25D0%25BE%25D0%25B3%25D0%25BE%25D0%25BD%2B%25D0%25BE%25D1%2582%2B%25D0%25B7%25D0%25B0%25D1%2581%25D0%25BE%25D1%2580%25D0%25BE%25D0%25B2&src_modal=%2Fmodal%2Faddressbook%3Fsrc_main%3D%252Fsearch%252F%253Ffrom_global%253Dtrue%2526text%253D%2525D1%252588%2525D0%2525B8%2525D0%2525BA%252B%2525D0%2525B2%2525D0%2525BE%2525D0%2525BB%2525D0%2525BE%2525D1%252581%2525D0%2525BE%2525D0%2525B3%2525D0%2525BE%2525D0%2525BD%252B%2525D0%2525BE%2525D1%252582%252B%2525D0%2525B7%2525D0%2525B0%2525D1%252581%2525D0%2525BE%2525D1%252580%2525D0%2525BE%2525D0%2525B2&tab=c',
        }
        json_data = {
            'geolocation': {
                'coords': {},
                'isAvailable': False,
            },
            'form': {
                'addressTail': 'Удмуртская Республика, Ижевск, Центральная площадь, 53',
                'apartment': '',
                'zipCode': '',
                'entrance': '',
                'floor': '',
                'intercom': '',
            },
            'map': {
                'viewport': {
                    'leftBottom': {
                        'latitude': 56.848496165252364,
                        'longitude': 53.20051086262973,
                    },
                    'rightTop': {
                        'latitude': 56.857319266296074,
                        'longitude': 53.209587457936124,
                    },
                },
                'zoom': 16,
                'previousCoordinates': {
                    'latitude': 56.852907975834725,
                    'longitude': 53.20504916028291,
                },
            },
        }
        response = self.session.post(
            'https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2',
            params=params,
            cookies=cookies,
            headers=self.headers,
            # json=json_data,
            impersonate="chrome110"
        ).cookies
        ic(response)
        return response

    def searchResultsV2(self, cookies, ua, headers, searh_text, page):
        # params = {
        #     'from_global': 'true',
        #     'page': page,
        #     'text': searh_text,
        #     # "tf_state": "RugZQyjFuYDNcKEefNQm-fpVv4VeHVcrEFZmfuKBQyIKO1cx"
        # }
        # params = {
        #     'category_was_predicted': 'true',
        #     'deny_category_prediction': 'true',
        #     'from_global': 'true',
        #     'page': page,
        #     'text': searh_text,
        #     # 'tf_state': 'e3EYXzH7HAcMY9i_BLVlQFgptMXaYbH2X5vUE_LZLbdeYKCP',
        # }
        params = {
            # '_fr': str(int(time.time())),
            'from_global': 'true',
            'text': str(searh_text),
            'page': str(page)
        }
        ic(params)
        # ic(cookies)
        response = self.session.get('https://www.ozon.ru/search/', params=params,
                                    cookies=cookies, headers=headers, impersonate=ua,
                                    timeout=30)
        # write to file
        with open('ozon.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        html = etree.HTML(response.text)
        data = html.xpath(
            '//div[contains(@id,"state-searchResultsV2")]/@data-state')
        ic(len(data))
        # print(data)
        data = json.loads(data[0])
        return data


if __name__ == '__main__':
    search_text = 'шик волосогон от засоров'
    ozon = Ozon_Spider()
    # cookies = ozon.Get_cookies()  # 需要科学
    # cookies = ozon.ChangeAddress(cookies)
    gencookies = GenCookie()
    cookies, ua, headers = gencookies.gen_cookie()

    writer = DataWriter('data.csv')
    str_today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    for page in range(1, 11):
        # page = 1
        time.sleep(3)
        data = ozon.searchResultsV2(cookies, ua, headers, search_text, page)
        print(len(data['items']))
        datas = ParseData(data)
        datas.parseData(writer, search_text, str_today, page)
    writer.close()
