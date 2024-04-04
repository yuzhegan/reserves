# encoding='utf-8

# @Time: 2024-01-14
# @File: %
#!/usr/bin/env

from icecream import ic
import os
from curl_cffi import requests
import random
from fake_useragent import UserAgent
from get_porxy import get_proxy


class GenCookie(object):
    def __init__(self):
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
        self.uaa = [
            "edge99",
            "edge101",
            "chrome99",
            "chrome100",
            "chrome101",
            "chrome104",
            "chrome107",
            "chrome110",
            "chrome116",
            "chrome119",
            "chrome120",
            "chrome99_android",
            "safari15_3",
            "safari15_5",
            "safari17_0",
            "safari17_2_ios",
            "chrome120",
            "safari17_0",
            "safari17_2_ios"
        ]
        self.session = requests.Session()
        # self.session.headers.update(self.headers)

    def gen_cookie(self):
        ua = random.choice(self.uaa)
        ic(ua)
        self.headers['user-agent'] = UserAgent().random
        # self.session.headers.update(self.headers)
        response = self.session.get('https://www.ozon.ru/',
                                    impersonate=ua, headers=self.headers, timeout=30,
                                    )
        response = self.session.post('https://www.ozon.ru/abt/result',
                                    impersonate=ua, headers=self.headers, timeout=30,
                                    )
        if "abt_data" not in response.cookies:
            print("获取cookie失败")
            proxies = random.choice(get_proxy())
            ic(proxies)
            ua = random.choice(self.uaa)
            response = self.session.get('https://www.ozon.ru/',
                                        impersonate=ua, headers=self.headers, proxies=proxies, timeout=30)
            if "abt_data" not in response.cookies:
                print("获取cookie二次失败")
        else:
            print("获取cookie成功")
        # 这种方式获取的cookies 需要科学
        cookies = response.cookies
        ic(cookies)
        return cookies, ua, self.headers

    def ChangeAddress(self, cookies, ua, headers, latitude, longitude):
        # 换经纬度就可以切换地址了
        url = f'/modal/commonDelivery?azimuth=0.504069202103&dt=1&lat={latitude}&long={longitude}&msid=030d9c7b-63a8-4442-b855-64d060c7abb1&neaf=f&nfr=t&pid=7&pv=2&pxlw=423.000000&src_main=%2Fsearch%2F%3Ffrom_global%3Dtrue%26text%3D%25D1%2588%25D0%25B8%25D0%25BA%2B%25D0%25B2%25D0%25BE%25D0%25BB%25D0%25BE%25D1%2581%25D0%25BE%25D0%25B3%25D0%25BE%25D0%25BD%2B%25D0%25BE%25D1%2582%2B%25D0%25B7%25D0%25B0%25D1%2581%25D0%25BE%25D1%2580%25D0%25BE%25D0%25B2&src_modal=%2Fmodal%2Faddressbook%3Fsrc_main%3D%252Fsearch%252F%253Ffrom_global%253Dtrue%2526text%253D%2525D1%252588%2525D0%2525B8%2525D0%2525BA%252B%2525D0%2525B2%2525D0%2525BE%2525D0%2525BB%2525D0%2525BE%2525D1%252581%2525D0%2525BE%2525D0%2525B3%2525D0%2525BE%2525D0%2525BD%252B%2525D0%2525BE%2525D1%252582%252B%2525D0%2525B7%2525D0%2525B0%2525D1%252581%2525D0%2525BE%2525D1%252580%2525D0%2525BE%2525D0%2525B2&tab=c'.format(
            latitude, longitude)
        print(url)
        params = {
            'url': url,
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
            headers=headers,
            # json=json_data,
            impersonate=ua
        )
        cookies = response.cookies
        return cookies


# if __name__ == '__main__':
#     gen_cookie = GenCookie()
#     gen_cookie.gen_cookie()

