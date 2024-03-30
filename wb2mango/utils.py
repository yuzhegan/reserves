# encoding='utf-8

# @Time: 2024-01-10
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import execjs
import time
from py_mini_racer import MiniRacer


# imageurl  搜索关键字basket-${t}.wbbasket.ru
# 送达日期  搜索关键字Доставка                завтра

with open("./wb2mango/delievry.js", "r", encoding="utf-8") as f:
    js = f.read()
ctx1 = MiniRacer()
ctx = ctx1.eval(js)

with open("./wb2mango/ImageUrl.js", "r", encoding="utf-8") as f:
    imgjs = f.read()
ctx2 = MiniRacer()
ctx2.eval(imgjs)


def AdPormotion(data, adpromotion):
    try:
        result = data["log"][adpromotion]
    except:
        result = ""
    return result
def GetdevileveyDay(time1, time2):
    time = int(time1) + int(time2)  # 两个时间相加 然后调用js函数转化为到达时间
    # ic(ctx.call("deliveryDateTxt", time))
    return ctx1.call("deliveryDateTxt", time)
def GetImageurl(id):
    id = str(id)
    hosts = ctx2.call("constructHostV2", id)
    if len(id) == 9:
        imageurl = hosts + '/vol' + id[:4] +"/part" + id[:6] + "/" + id + '/images/c516x688/1.webp'
    elif len(id) == 8:
        imageurl = hosts + '/vol' + id[:3] +"/part" + id[:5] + "/" + id + '/images/c516x688/1.webp'
    elif len(id) == 7:
        imageurl = hosts + '/vol' + id[:2] +"/part" + id[:4] + "/" + id + '/images/c516x688/1.webp'

    return imageurl

