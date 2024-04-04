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

    def genRequestToken(self, cookies, headers):
        json_data = {
            'return_url': 'https://seller.ozon.ru/app/dashboard',
            'webhook_url': 'https://seller.ozon.ru/app/dashboard',
        }

        response = self.session.post('https://seller.ozon.ru/api/ozon-id/request-token',
                                     cookies=cookies, headers=headers, json=json_data).json()
        data = response["result"]["token"]
        ic(data)
        return data

    def submitEmailCode(self, cookies, headers, request_token):
        ic(self.session.cookies),
        json_data = {
            'isVerifiedEmail': False,
            'isSecondFactor': False,
            'isValuableAccount': False,
            'firstOtpSentToEmail': False,
            'activeOtpSentToEmail': False,
            'isRecognized': False,
            'authRequestToken': 'eyJhbGciOiJIUzI1NiIsIm96b25pZCI6Im5vdHNlbnNpdGl2ZSIsInR5cCI6IkpXVCJ9.eyJtb2RlIjoxLCJvcmlnaW4iOjYsIndlYmhvb2tfdXJsIjoiaHR0cHM6Ly9zZWxsZXIub3pvbi5ydS9hcHAvZGFzaGJvYXJkL21haW4iLCJwYXlsb2FkIjpudWxsLCJyZXR1cm5fdXJsIjoiaHR0cHM6Ly9zZWxsZXIub3pvbi5ydS9hcHAvZGFzaGJvYXJkL21haW4iLCJyZWZlcmVyX3BhZ2VfdHlwZSI6InNlbGxlcl9jZW50ZXIiLCJyZXF1aXJlZF9maWVsZHMiOls1LDYsMTBdLCJwYXRjaF91c2VyX2FjY291bnRfcGFyYW1zIjpudWxsLCJiaW5kX2Nhc19pZCI6ZmFsc2UsInVzZV9vaWRjIjpmYWxzZSwib2lkY19kYXRhIjp7fSwiYm91bmRfdXNlcl9pZCI6MCwiaGlkZV9sb2dvIjpmYWxzZSwiYmluZF9yb2xlcyI6e30sImZvcmNlX2xvZ291dCI6ZmFsc2UsInRva2VuX2lkIjoiIiwicmV2b2NhYmxlIjpmYWxzZSwiY2FuX3NraXBfcGF0Y2giOmZhbHNlLCJiaW5kX2FkX2FjY291bnQiOmZhbHNlLCJleHAiOjE3MTIzMDI3NTQsImlhdCI6MTcxMjIxNjM1NCwiaXNzIjoib3pvbmlkIn0.kdftYnDt6zzrGqRYMBw-NM3eBFlsTMVaMDi8MfKQTio',
            'isAlphaNumericOtp': False,
            'hideHints': False,
            'csrfToken': 'eyJhbGciOiJIUzI1NiIsIm96b25pZCI6Im5vdHNlbnNpdGl2ZSIsInR5cCI6IkpXVCJ9.eyJyZXF1ZXN0VW5peFRpbWUiOjE3MTIyMTY5NTIsInNlc3Npb25JZCI6IlBfLUFoWk56VGY2VUxackZvSFNIOWcifQ.W-0lr_XfYjNlkfD_x-UcjSaqI5ZXfwsUI5NaLcjUlOs',
            'isOtpExpired': False,
            'isAdsAllowed': False,
            'isVerifiedEmailError': False,
            'isForceSmsOtp': False,
            'IsEmailRegistrationState': False,
            'isForceFlashCallOtp': False,
            'otpSentToPush': False,
            'otpSentToChainPushNc': False,
            'countryCode': 'CN',
            'widgetName': 'csma.loginOrRegistration',
            'isSeller': False,
            'isAccountRecoveryAllowed': False,
            'sellerCountry': '',
            'secondFactorCase': '',
            'hasBankAccount': False,
            'hasRecentActiveMobileSession': False,
            'email': 'luouse@gmail.com',
        }

        response = requests.post(
            'https://www.ozon.ru/api/composer-api.bx/_action/emailOtpEntry',
            cookies=cookies,
            headers=headers,
            json=json_data,
        ).json()
        ic(response)

        return

    def ozonApiV3(self, cookies, headers, request_token):
        json_data = {
            'email': 'luouse@gmail.com',
            'isVerifiedEmail': False,
            'isSecondFactor': False,
            'isValuableAccount': False,
            'firstOtpSentToEmail': False,
            'activeOtpSentToEmail': False,
            'isRecognized': False,
            'authRequestToken': 'eyJhbGciOiJIUzI1NiIsIm96b25pZCI6Im5vdHNlbnNpdGl2ZSIsInR5cCI6IkpXVCJ9.eyJtb2RlIjoxLCJvcmlnaW4iOjYsIndlYmhvb2tfdXJsIjoiaHR0cHM6Ly9zZWxsZXIub3pvbi5ydS9hcHAvZGFzaGJvYXJkL21haW4iLCJwYXlsb2FkIjpudWxsLCJyZXR1cm5fdXJsIjoiaHR0cHM6Ly9zZWxsZXIub3pvbi5ydS9hcHAvZGFzaGJvYXJkL21haW4iLCJyZWZlcmVyX3BhZ2VfdHlwZSI6InNlbGxlcl9jZW50ZXIiLCJyZXF1aXJlZF9maWVsZHMiOls1LDYsMTBdLCJwYXRjaF91c2VyX2FjY291bnRfcGFyYW1zIjpudWxsLCJiaW5kX2Nhc19pZCI6ZmFsc2UsInVzZV9vaWRjIjpmYWxzZSwib2lkY19kYXRhIjp7fSwiYm91bmRfdXNlcl9pZCI6MCwiaGlkZV9sb2dvIjpmYWxzZSwiYmluZF9yb2xlcyI6e30sImZvcmNlX2xvZ291dCI6ZmFsc2UsInRva2VuX2lkIjoiIiwicmV2b2NhYmxlIjpmYWxzZSwiY2FuX3NraXBfcGF0Y2giOmZhbHNlLCJiaW5kX2FkX2FjY291bnQiOmZhbHNlLCJleHAiOjE3MTIzMDI3NTQsImlhdCI6MTcxMjIxNjM1NCwiaXNzIjoib3pvbmlkIn0.kdftYnDt6zzrGqRYMBw-NM3eBFlsTMVaMDi8MfKQTio',
            'otpId': 636516911,
            'isAlphaNumericOtp': False,
            'hideHints': False,
            'csrfToken': 'eyJhbGciOiJIUzI1NiIsIm96b25pZCI6Im5vdHNlbnNpdGl2ZSIsInR5cCI6IkpXVCJ9.eyJyZXF1ZXN0VW5peFRpbWUiOjE3MTIyMTY0NTIsInNlc3Npb25JZCI6IlBfLUFoWk56VGY2VUxackZvSFNIOWcifQ.dk0eOcZH5-qpao2CfDh6_Q5ZmYX8elL28Q2Ik0jcMQs',
            'isOtpExpired': False,
            'isAdsAllowed': True,
            'isVerifiedEmailError': False,
            'isForceSmsOtp': False,
            'IsEmailRegistrationState': False,
            'isForceFlashCallOtp': False,
            'otpSentToPush': False,
            'otpSentToChainPushNc': False,
            'countryCode': 'CN',
            'widgetName': 'csma.loginOrRegistration',
            'isSeller': False,
            'isAccountRecoveryAllowed': False,
            'sellerCountry': '',
            'secondFactorCase': '',
            'hasBankAccount': False,
            'hasRecentActiveMobileSession': False,
            'otp': input('请输入验证码：'),
        }

        response = requests.post(
            'https://www.ozon.ru/api/composer-api.bx/_action/emailOtpEntry',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        return

    def ozonSearchV3(self, cookies, headers):
        headers['x-o3-app-name'] = 'seller-ui'
        headers['x-o3-company-id'] = '1501369'
        headers['x-o3-language'] = 'zh-Hans'
        cookies['__Secure-access-token'] = '4.160357014.AA3RT3XZSMKpkQ4IQsZqJg.91.AdIXaoj-NVGgqL3b8I60BWocNwDdnA4yQY7tI9RiaZXJIqAyvekip__JRgjiOviovY3qTYbxY9sFJWbdqqjJ3qU.20240402125018.20240404120743.RGPQ2ombt7qBZK8yBHOrPTlB90arSX9fNXJO83T4Gy0'
        json_data = {
            'filter': {
                'stock': 'any_stock',
                'sku': '503746894',
            },
            'sort': {
                'key': 'sum_rating',
            },
            'limit': '50',
            'offset': '0',
        }

        response = self.session.post(
            'https://seller.ozon.ru/api/site/seller-analytics/what_to_sell/data/v3',
            cookies=cookies,
            headers=headers,
            json=json_data,
        ).json()
        ic(response)
        return response


if __name__ == '__main__':
    ozon = Ozon_Spider()
    gencookies = GenCookie()
    cookies, ua, headers = gencookies.gen_cookie()
    # request_token = ozon.genRequestToken(cookies, headers)
    # ozon.submitEmailCode(cookies, headers, request_token)
    # ozon.ozonApiV3(cookies, headers, request_token)
    ozon.ozonSearchV3(cookies, headers)
