# encoding='utf-8

# @Time: 2023-10-25
# @File: %
#!/usr/bin/env
from icecream import ic
import os
from selenium import webdriver
import time

# from selenium.webdriver import Chrome 
# from selenium.webdriver import ChromeOptions 
#
# option = ChromeOptions() 
# # 实现规避检测
# option.add_argument("--disable-blink-features=AutomationControlled")
# option.add_experimental_option('excludeSwitches', ['enable-automation']) 
# driver = Chrome(options=option)

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)
driver.maximize_window()


driver.get("https://login.taobao.com/")

# read c.js 
with open(os.path.join(os.path.dirname(__file__), 'genpasswd2.py'), 'r', encoding='utf-8') as f:
    js = f.read()
    # ruan c.js the function test and ouptut test value
    output = driver.execute_script(js)
    time.sleep(6)
    print(output)
    # ic(output['permanent_id'])
    # ic(output['sign'])


