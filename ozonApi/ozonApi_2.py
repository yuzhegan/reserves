# encoding='utf-8

# @Time: 2024-04-02
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests

import requests

cookies = {
    # '__Secure-ab-group': '62',
    # 'xcid': '8a9b00adbb329627fa10bd86ded4ba71',
    # '__Secure-ext_xcid': '8a9b00adbb329627fa10bd86ded4ba71',
    # 'guest': 'true',
    # '__Secure-user-id': '153179496',
    # 'is_adult_confirmed': '',
    # 'is_alco_adult_confirmed': '',
    # 'bacntid': '3741873',
    # 'contentId': '1654428',
    'x-o3-language': 'zh-Hans',
    'abt_data': '76280bebf0fff72135ded588b0a9ec3c:bb45c414d8872cf670600ea60dfacd5243a64fe8de1d8df75f7f1c8704a573ccbcac49b4c47a7c177462a2918d329d4b314685ca68c577b8a855aee1d3f158f674578792aee593decd7bcb3d8076fdab8d50dc6c90c9819a6b3cf621bc182e01edf72e499cf2c59d1d5dae57d80fdbba14fc88a8bbf337e2e588ec34e82cdc6446563451d8b44e85a358b15b720e33f597e2069fe93d826e8ab048de47bb235f8aa94a54b3a695f05f8254ffa874fa1204f09d2ebaf9db628677d4121605e25813ae82c248c2f5e1475422f94d3f2df9db94417779e0ba1a4009b633261cd71d184dbb183df6a5836dd52a421df02975d497731d4830b1b4e25fb7cb24fec9deacfffbb7cda65c1bae2fe08dfc3d15f7bb78dd82e392fb24476e6cddb08a216a0b6a5bc72ea9dea145b087d3659cf9c91ba6a4d937d6dc34fe7dab450bd7b57189ef60b341bd346229df0fcc957de728',
    '__Secure-access-token': '4.153179496.fWFCUm3hQxWjn82auRWFGw.62.AQv1zRpn2rayYgs-GvnBzNhSLdjYBqo4Bl-ZseLbdEt_F57K06jbdc0gKNnaidbF8gva5LDwdWA5G1phrCZ_CGs.20240115055703.20240402121000.l3CUZ71nXWV5HHQr4xCWmkWL82X7tNLk_tFaHdyHKbs',
    # '__Secure-refresh-token': '4.153179496.fWFCUm3hQxWjn82auRWFGw.62.AQv1zRpn2rayYgs-GvnBzNhSLdjYBqo4Bl-ZseLbdEt_F57K06jbdc0gKNnaidbF8gva5LDwdWA5G1phrCZ_CGs.20240115055703.20240402121000.wQBtXXl1M7oHNZKP5y4nS1mtlWUzbGhDX4WRw8gtWVc',
    # 'cf_clearance': 'xfA9NBBhd2R3SqTntrHFJUTo.qaxO3y9M9XhOq8OoTw-1712053639-1.0.1.1-3HGogOTkW8SHNe_G1SRLuoJZJnAohcLG8muFCF.id2.6iuCWpnX7uEpn9I7rwiEjudQUxBog_KCeBXt7upkCww',
    # '__cf_bm': '.xUXh45ogWgdP_XA7sKsARXckmk1ir5wJcUaQTa6Kug-1712054580-1.0.1.1-FT6EfdnkLpTySYpD_8Rlkpn_DaDAZxu0Y4RVBFpvdYBloo0f9VCqgls0r6VwwCkOZ__qWjcQ9NnvS8Ar6M345g',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-Hans',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://seller.ozon.ru',
    'pragma': 'no-cache',
    'referer': 'https://seller.ozon.ru/app/analytics/what-to-sell/ozon-bestsellers',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"123.0.6312.86"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="123.0.6312.86", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.86"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-o3-app-name': 'seller-ui',
    'x-o3-company-id': '1654428',
    'x-o3-language': 'zh-Hans',
    'x-o3-page-type': 'what-to-sell',
}

json_data = {
    'filter': {
        'stock': 'any_stock',
    },
    'sort': {
        'key': 'sum_rating',
    },
    'limit': '50',
    'offset': '0',
}

response = requests.post(
    'https://seller.ozon.ru/api/site/seller-analytics/what_to_sell/data/v3',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
ic(response)
