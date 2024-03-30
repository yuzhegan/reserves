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
import polars as pl
import random
# from CookiePool import CookiePool


class Ozon_Spider:
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
        self.session = requests.Session()

    def Get_cookies(self):
        response = self.session.get('https://www.ozon.ru/',
                                impersonate="chrome110", headers=self.headers, timeout=30)
        response = self.session.get('https://www.ozon.ru/abt/result',
                                impersonate="chrome110", headers=self.headers, timeout=30).cookies
        cookies = response
        ic(cookies)
        return cookies

    def searchResultsV2(self, cookies, searh_text, page):
        params = {
            'category_was_predicted': 'true',
            'deny_category_prediction': 'true',
            'from_global': 'true',
            'page': page,
            'text': searh_text,
            # 'tf_state': 'e3EYXzH7HAcMY9i_BLVlQFgptMXaYbH2X5vUE_LZLbdeYKCP',
        }
        params2 = {
            'from_global': 'true',
            'page': page,
            'text': searh_text,
            # 'tf_state': '9Zye8loRlfNjrYp09M2p8IFkgmWC-tpWi3enguuQgJCRYY4T',
        }
        response = self.session.get('https://www.ozon.ru/search/', params=params,
                                cookies=cookies, headers=self.headers, impersonate="chrome110")
        # write to file
        # with open('ozon.txt', 'w', encoding='utf-8') as f:
        #     f.write(response.text)
        html = etree.HTML(response.text)
        data = html.xpath(
            '//div[contains(@id,"state-searchResultsV2")]/@data-state')
        ic(len(data))
        if len(data) == 0:
            response = self.session.get('https://www.ozon.ru/search/', params=params2,
                                    cookies=cookies, headers=self.headers, impersonate="chrome110")

            html = etree.HTML(response.text)
            data = html.xpath(
                '//div[contains(@id,"state-searchResultsV2")]/@data-state')
            if len(data) == 0:
                ic("未能获取达第" + str(page) + "页数据")
                return None
        # pages = self.getFullPage(html)
        datas = json.loads(data[0])
        ic(len(datas))
        # with open('ozon.json', 'w', encoding='utf-8') as f:
        #     f.write(json.dumps(data, indent=4, ensure_ascii=False))
        return datas

    def reGensearchResult(self, searh_text, page):
        # cookies 失效 重新生成 再去爬数据
        cookies = self.Get_cookies()
        try:
            data = self.searchResultsV2(cookies, searh_text, page)
        except Exception as e:
            data = None
        return data, cookies

    def getFullPage(self, response):
        pages = len(response.xpath(
            '//*[@id="layoutPage"]/div[1]/div[2]/div[2]/div[2]/div[5]/div[2]/div/div/div/a')) - 1
        return pages

from writeLogo import WriteLogo


if __name__ == '__main__':
    # search_text = 'мыльная бабочка'
    # 读取错误日志  断点续爬
    errorlog = WriteLogo("./errlog.txt")  # 
    last_search_text = None
    if os.path.exists("./errlog.txt"):
        contents = errorlog.readLogo().split("\n")
        ic(contents)
        contents = list(set(contents)) # 去重
        ic(len(contents))
        ozon = Ozon_Spider()
        cookies = ozon.Get_cookies()
        str_today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        for content in contents:
            if content != "":
                search_text, page = content.split("\t")
                ic(search_text, page)
                time.sleep(random.randint(1, 3))
                try:
                    data = ozon.searchResultsV2(cookies, search_text, page)
                except Exception as e:
                    ic(e)
                    time.sleep(random.randint(6, 10))
                    data, cookies = ozon.reGensearchResult(search_text, page)
                if data:  # 如果获取到数据
                    print(len(data['items']))
                    datas = ParseData(data)
                    items = datas.parseData(search_text, str_today, page)
                    if len(data['items']) < 36:
                        ic("下一页没有数据了")
                        break
                else:  # 如果未获取到数据
                    data, cookies = ozon.reGensearchResult(search_text, page)
                    if data:
                        print(len(data['items']))
                        datas = ParseData(data)
                        items = datas.parseData(search_text, str_today, page)
                    else:
                        ic("未能获取到" + str(search_text) + "第" + str(page) + "页数据")
                        log_txt = search_text + "\t" + str(page) # 写入错误日志
                        errorlog.writeLogo(log_txt)
                        continue
        last_search_text = contents[-2].split("\t")[0]
        errorlog.deleteLogo()


    # 从excel中读取搜索词
    df = pl.read_excel('./客户搜素词.xlsx')
    df = df.filter(pl.col('openOff') == 'on')
    # 删除空行
    search_text_list = df.drop_nulls()['searchTerm'].to_list()
    if last_search_text:
        search_text_list = search_text_list[search_text_list.index(last_search_text) + 1:]
    # 从错误日志中读取最后一个搜索词 从该搜索词开始爬取

    ic(len(search_text_list))
    ozon = Ozon_Spider()
    cookies = ozon.Get_cookies()
    str_today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    for search_text in search_text_list:
        time.sleep(random.randint(3, 5))
        ic(search_text)
        for page in range(1, 8):
            time.sleep(random.randint(1, 3))
            try:
                data = ozon.searchResultsV2(cookies, search_text, page)
            except Exception as e:
                ic(e)
                time.sleep(random.randint(6, 10))
                data, cookies = ozon.reGensearchResult(search_text, page)
            if data:  # 如果获取到数据
                print(len(data['items']))
                datas = ParseData(data)
                items = datas.parseData(search_text, str_today, page)
                if len(data['items']) < 36:
                    ic("下一页没有数据了")
                    break
            else:  # 如果未获取到数据
                data, cookies = ozon.reGensearchResult(search_text, page)
                if data:
                    print(len(data['items']))
                    datas = ParseData(data)
                    items = datas.parseData(search_text, str_today, page)
                else:
                    ic("未能获取到" + str(search_text) + "第" + str(page) + "页数据")
                    log_txt = search_text + "\t" + str(page) # 写入错误日志
                    errorlog.writeLogo(log_txt)
                    continue
            # ic(items)
        # writer.close()
        # writer.close()
