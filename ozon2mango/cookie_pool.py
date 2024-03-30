# encoding='utf-8
# @Time: 2024-01-05
# @File: %
#!/usr/bin/env
from icecream import ic
import os
# from curl_cffi import requests
from BiteApi.bit_pyppeteer import *

class CookiePool:
    def __init__(self):
        self.cookies = None
    def Get_cookies(self):
        browser_id = createBrowser('ozon')
        openBrowser(browser_id)
        bit_browser = BitBrowser(browser_id)
        print(bit_browser.cookies)
        closeBrowser(browser_id)
        deleteBrowser(browser_id)


if __name__ == '__main__':
    cookies  = CookiePool().Get_cookies()
    # 转字典
    print(cookies.cookies)


