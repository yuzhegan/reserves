# encoding='utf-8

# @Time: 2024-01-10
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import execjs

with open('./wildberries/delievry.js', 'r', encoding='utf-8') as f:
    jscode = f.read()
ctx = execjs.compile(jscode)
result = ctx.call('deliveryDateTxt', 136)
ic(result)
